from django.db import models
from suceco._constants import STATUS

class Species(models.Model):

  id = models.AutoField(primary_key=True)
  scientific_name = models.CharField(max_length=1000, unique=True, help_text= 'Species')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=1)

  def __str__(self) :
      return self.scientific_name

  class Meta :
      ordering = ['scientific_name']

