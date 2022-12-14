from django.db import models
from suceco._constants import STATUS, DOMAINS

class Forest(models.Model) :

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    domain = models.CharField(max_length=100, choices=DOMAINS)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.name

    class Meta :
        ordering = ['name']

