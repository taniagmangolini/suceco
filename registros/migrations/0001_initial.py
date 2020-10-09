# Generated by Django 3.0.3 on 2020-10-09 18:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formacaoflorestal', '0002_auto_20201009_1752'),
        ('especies', '0003_auto_20201009_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('estagio', models.CharField(choices=[('pioneira', 'Pioneira'), ('secundaria_inicial', 'Secundaria Inicial'), ('secundaria_tardia', 'Secundaria Tardia'), ('umbrofila', 'Umbrofila'), ('secundaria', 'Secundaria')], max_length=50)),
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MT', 'MT'), ('MS', 'MS'), ('PA', 'PA'), ('PE', 'PE'), ('PB', 'PB'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RR', 'RR'), ('RS', 'RS'), ('RO', 'RO'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=50)),
                ('status', models.CharField(choices=[('active', 'Ativo'), ('inactive', 'Inativo')], default='Ativo', max_length=15)),
                ('referencia', models.CharField(default='', max_length=1000)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='especies.Especie')),
                ('formacao_florestal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formacaoflorestal.FormacaoFlorestal')),
            ],
        ),
    ]
