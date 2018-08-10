from django.urls import path
from . import views

app_name = "cuentas"
urlpatterns = [
    path('login/', views.login_usuario, name="login"),
    path('logout/', views.logout_usuario, name='logout'),
    path('registrar/', views.registrar_usuario, name="registrar")
]