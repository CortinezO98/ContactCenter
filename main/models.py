from django.db import models
from django.contrib.auth.models import User

class Agente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.IntegerField()

class Cliente(models.Model):
    documento = models.IntegerField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    celular = models.IntegerField()    

class TipoSolicitud(models.Model):
    nombre = models.CharField(max_length=100)

class Solicitud(models.Model):
    tipoSolicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE)
    llamaEnNombrePropio = models.BooleanField()
    seAgendaCita = models.BooleanField()
    quedaCitaEnEspera = models.BooleanField()
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

class Sede(models.Model):
    nombre = models.CharField(max_length=100)

class Medico(models.Model):
    nombre = models.CharField(max_length=100)

class Cita(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

class CitaCliente(models.Model):
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
