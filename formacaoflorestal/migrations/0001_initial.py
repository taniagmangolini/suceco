# Generated by Django 3.0.3 on 2020-10-09 17:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormacaoFlorestal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=500)),
                ('dominio', models.CharField(choices=[('amazonico', 'Amazonia'), ('mata_atlantica', 'Inativo'), ('mata_atlantica', 'Mata Atlantica'), ('caatinga', 'Caatinga'), ('cerrado', 'Cerrado'), ('pantanal', 'Pantanal'), ('pradarias', 'Pradarias'), ('', '')], default='', max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=15)),
            ],
        ),
    ]
