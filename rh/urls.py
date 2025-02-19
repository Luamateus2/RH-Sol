from django.urls import path
from .views import home_views,employee_views

urlpatterns = [
    path('login',home_views.login,name='login page'),
    path('signup',home_views.signup,name='page signup'),
    path('',home_views.home,name='home'),
]
