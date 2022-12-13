from django.core.management.base import BaseCommand
from django.conf import settings
from species.models import Species
from forest.models import Forest
from reference.models import Reference
from register.models import Register
import os
import csv

class Command(BaseCommand):
    '''
        Script to populate tables.
        This command can be called executing: python manage.py firstload
    '''
    def handle(self, *args, **options):
        self.stdout.write('Loading forests...')
        forests_file = 'register/management/formacaoflorestal.csv'
        with open(os.path.join(settings.BASE_DIR, forests_file), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not Forest.objects.filter(name=str(row[0]), domain=str(row[1])).exists():
                    Forest.objects.create(name=str(row[0]), domain=str(row[1]))
                
        self.stdout.write('Loading references...')
        references_file = 'register/management/references.csv'
        with open(os.path.join(settings.BASE_DIR, references_file), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not Reference.objects.filter(url=str(row[0]), publication=str(row[1])).exists():
                    Reference.objects.create(url=str(row[0]), publication=str(row[1]))

        self.stdout.write('Loading species...')
        species_file = 'register/management/especies.csv'   
        with open(os.path.join(settings.BASE_DIR, species_file), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not Species.objects.filter(scientific_name=str(row[0])).exists():
                    Species.objects.create(scientific_name=str(row[0]))

        self.stdout.write('Loading registers...')
        registers_file = 'register/management/registros.csv'    
        with open(os.path.join(settings.BASE_DIR, registers_file), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                stage = str(row[0])
                state = str(row[1])
                species = Species.objects.filter(scientific_name=str(row[2]))[0]
                forest = Forest.objects.filter(name=str(row[3]))[0]
                self.stdout.write(row[4])
                reference = Reference.objects.filter(publication__contains=str(row[4]))[0]
                if not Register.objects.filter(stage=stage, state=state, forest=forest,
                                               reference=reference, species=species).exists():
                    Register.objects.create(stage=stage, state=state, forest=forest,
                                            reference=reference,species=species)

