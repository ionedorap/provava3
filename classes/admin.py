#coding:utf-8
from django.contrib import admin
from models import *

class usuarioAdmin(admin.ModelAdmin):
	list_display = ['nome','area','nivel']
	
class localAdmin(admin.ModelAdmin):
	list_display = ['nome','area','nivel']

class advertenciaAdmin(admin.ModelAdmin):
	list_display = ['usuario','local','entrada']

class acessoAdmin(admin.ModelAdmin):
	list_display = ['usuario','local','entrada','saida']


admin.site.register(usuario, usuarioAdmin)
admin.site.register(advertencia, advertenciaAdmin) 
admin.site.register(local, localAdmin) 
admin.site.register(acesso, acessoAdmin) 




