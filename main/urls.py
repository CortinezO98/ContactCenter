from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crearCliente/", views.crearCliente, name="crearCliente"),
    path("crearSolicitud/", views.crearSolicitud, name="crearSolicitud"),
    path("vistaSolicitud/<int:id>", views.vistaSolicitud, name="vistaSolicitud"),
    path("agendarCita/", views.agendarCita, name="agendarCita"),
    path("accounts/login/", views.Login, name="login"),
    path('logout/', views.Logout, name='logout'),
]