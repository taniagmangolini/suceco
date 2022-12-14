from reference.models import Reference
from django.db import models
from species.models import Species
from forest.models import Forest
from reference.models import Reference
from suceco._constants import STAGES, STATUS, STATES

class Register(models.Model) :

    id = models.AutoField(primary_key=True)

    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.SET_NULL, null=True)
    reference = models.ForeignKey(Reference, on_delete=models.SET_NULL, null=True)
    
    stage = models.CharField(max_length=50, choices=STAGES)
    state = models.CharField(max_length=50, choices=STATES)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    status = models.IntegerField(choices=STATUS, default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return '-'.join([str(self.id), self.species.name, self.forest.name])

