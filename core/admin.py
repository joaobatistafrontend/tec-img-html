from django.contrib import admin
from .models import Local,Opcoes, Agenda
# Register your models here.

@admin.register(Agenda)
class AgendaADM(admin.ModelAdmin):
     list_display = ['nome', 'email', 'local','opcao', 'local', 'data', 'protocolo']

@admin.register(Local)
class LocalADM(admin.ModelAdmin):
     list_display = ['cidade', 'endereco', 'numeracao', 'logradouro', 'mapa_link']

@admin.register(Opcoes)
class OpcoeslADM(admin.ModelAdmin):
     list_display = ['opcoes']