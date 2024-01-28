from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Agente)
admin.site.register(TipoSolicitud)
admin.site.register(Solicitud)
admin.site.register(Especialidad)
admin.site.register(Sede)
admin.site.register(Medico)
admin.site.register(Cita)
admin.site.register(CitaCliente)