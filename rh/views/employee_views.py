from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from ..models import Employee, Department

def register_employee(request):
    if request.method == 'POST':
        name = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        birth_date = request.POST.get('dt_nascimento')
        ctps = request.POST.get('ctps')
        department_id = request.POST.get('departamento')  # Obtém o ID do departamento

        # Verificar se os campos obrigatórios foram preenchidos
        if name and cpf and rg and birth_date and ctps and department_id:
            fields_and_messages = {
                'cpf': 'CPF já cadastrado!!',
                'rg': 'RG já cadastrado!',
                'ctps': 'CTPS já cadastrado!'
            }

            for field, message in fields_and_messages.items():
                if Employee.objects.filter(**{field: locals()[field]}).exists():
                    messages.error(request, message)
                    return render(request, 'rh/home.html')

            try:
                department = Department.objects.get(id=department_id)  # Pega o departamento pelo ID
                employee = Employee(
                    name=name,
                    cpf=cpf,
                    rg=rg,
                    birth_date=birth_date,
                    ctps=ctps,
                    department=department  # Atribui o departamento ao funcionário
                )
                employee.save()
                messages.success(request, 'Funcionário cadastrado com Sucesso!')
                return render(request, 'rh/home.html')

            except Department.DoesNotExist:
                messages.error(request, 'Departamento inválido!')
                return render(request, 'rh/home.html')

            except IntegrityError as e:
                messages.error(request, 'Não foi possível realizar o cadastro!')
                return render(request, 'rh/home.html')

        else:
            messages.error(request, 'Falta preencher os campos obrigatórios!')
            return render(request, 'rh/home.html')

    # Caso o método não seja POST, renderize a página com a lista de departamentos para escolha
    departments = Department.objects.all()
    return render(request, 'rh/index.html', {'departments': departments})

def update_employee(request, employee_id):
    # Obtém o funcionário com o ID fornecido
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        name = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        birth_date = request.POST.get('dt_nascimento')
        ctps = request.POST.get('ctps')
        department_id = request.POST.get('departamento')  # Obtém o ID do departamento

        # Verificar se todos os campos obrigatórios foram preenchidos
        if name and cpf and rg and birth_date and ctps and department_id:
            try:
                department = Department.objects.get(id=department_id)  # Obtém o departamento pelo ID

                # Atualiza os dados do funcionário
                employee.name = name
                employee.cpf = cpf
                employee.rg = rg
                employee.birth_date = birth_date
                employee.ctps = ctps
                employee.department = department  # Atribui o departamento ao funcionário
                employee.save()

                messages.success(request, 'Funcionário atualizado com sucesso!')
                return redirect('funcionarios_list')  # Substitua com a URL correta

            except Department.DoesNotExist:
                messages.error(request, 'Departamento inválido!')
                return render(request, 'rh/alterar_funcionario.html', {'employee': employee})

            except IntegrityError:
                messages.error(request, 'Não foi possível realizar a alteração do funcionário!')
                return render(request, 'rh/home.html')

        else:
            messages.error(request, 'Falta preencher os campos obrigatórios!')
            return render(request, 'rh/alterar_funcionario.html', {'employee': employee})

    # Caso o método não seja POST, exibe os dados atuais do funcionário para edição
    departments = Department.objects.all()  # Lista de departamentos
    return render(request, 'rh/alterar_funcionario.html', {'employee': employee, 'departments': departments})


def delete_employee(request,employee_id):
    employee = get_object_or_404(Employee,id=employee_id)
    if request.method =='POST':
      try:
        employee.delete()
        messages.success(request,'Cliente excluído com sucesso!')
      except Exception as e:
          messages.error(request,'Ocorreu um erro ao excluir o funcionário!')
          return render(request,'rh/home.html')
    return render(request,'rh/home.html')