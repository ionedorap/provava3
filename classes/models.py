#coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError

NIVEL = [
    ('1','livre'),
	('2','reservado'),
	('3','restrito'),
	]
	

class usuario(models.Model):
	nome = models.CharField('Nome',max_length=100,null=True)
	area = models.CharField('Area de atuação',max_length=100,null=True)
	nivel = models.CharField('Nível de Acesso',max_length=5,choices=NIVEL,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.nome, self.nivel)


class local(models.Model):
	nome = models.CharField('Nome',max_length=100,null=True)
	area = models.CharField('Area',max_length=100,null=True)
	nivel = models.IntegerField('Nível de Acesso',max_length=1,choices=NIVEL,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.nome, self.nivel)
		
class advertencia(models.Model):
	usuario = models.ForeignKey(usuario,verbose_name="usuario",null=True)
	local = models.ForeignKey(local,verbose_name="Local",null=True)
	entrada = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.usuario, self.local)

class acesso(models.Model):
	usuario = models.ForeignKey(usuario,verbose_name="usuario",null=True)
	local = models.ForeignKey(local,verbose_name="Local",null=True)
	entrada = models.DateTimeField(auto_now=True)
	saida = models.TimeField(verbose_name="Saida",null=True,blank=True)
	
	def clean(self):	
		a = "%s" %  (self.usuario.nivel)
		b = "%s" % (self.local.nivel)
		if a != b:
			raise ValidationError("Este usuário não tem o poder de acessar este local !! ")
		
		
		query = acesso.objects.filter(usuario=self.usuario, saida__isnull=True)
		if query and not self.id:	
			adv = advertencia()
			adv.usuario = self.usuario
			adv.local = self.local
			adv.entrada = self.entrada
			adv.save()
			raise ValidationError("Usuário ainda não deu baixa na sessão atual!")


	
	
			
		
			4
	
	
	


