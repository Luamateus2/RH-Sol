from django.urls import path
from .views import employee_views, user_views

urlpatterns = [
    path('login',user_views.authenticate_user,name='login page'),
    path('signup',user_views.add_user,name='page signup'),
    path('home',employee_views.register_employee,name='register'),
]
