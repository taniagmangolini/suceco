from django.db import models
import uuid # Required for unique book instances

class Especie(models.Model):
  STATUS = (
   ('Ativo', 'Ativo'),
   ('Inativo', 'Inativo')
  )
  
  #Primary 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  nome  = models.CharField(max_length=1000, unique=True, help_text= 'Espécie')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  status = models.CharField(max_length=15, choices=STATUS, default='Ativo', help_text='Status')

  def __str__(self) :
      return self.nome

  class Meta :
      ordering = ["nome"]