# Generated by Django 3.2.16 on 2022-12-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
    ]
