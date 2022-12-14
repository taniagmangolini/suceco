from django.db import models
from suceco._constants import STATUS

class Reference(models.Model) :

    id = models.AutoField(primary_key=True)
    publication = models.CharField(max_length=1000, default= '')
    url = models.CharField(max_length=1000, default= '')
    status = models.IntegerField(choices=STATUS, default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return '-'.join([str(self.id), self.publication, self.url])

