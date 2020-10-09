from django.db import models
import uuid # Required for unique book instances

'''class Especie(models.Model):
  STATUS = (
   ('active', 'Ativo'),
   ('inactive', 'Inativo')
  )
  
  #Primary 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  
  nome  = models.CharField(max_length=1000)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  status = models.CharField(max_length=15, choices=STATUS)
'''
class FormacaoFlorestal(models.Model):

  STATUS = (
   ('active', 'Ativo'),
   ('inactive', 'Inativo')
  )
  
  DOMINIOS = (
   ('amazonico', 'Amazonia'),
   ('mata_atlantica', 'Inativo'),
   ('mata_atlantica', 'Mata Atlantica'),
   ('caatinga', 'Caatinga'),
   ('cerrado', 'Cerrado'),
   ('pantanal', 'Pantanal'),
   ('pradarias', 'Pradarias'),
   ('', '')
  )
   
  #Primary 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
   
  nome = models.CharField(max_length=500)
  dominio = models.CharField(max_length=100, choices=DOMINIOS, default='')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  status = models.CharField(max_length=15, choices=STATUS)
    
    

  


