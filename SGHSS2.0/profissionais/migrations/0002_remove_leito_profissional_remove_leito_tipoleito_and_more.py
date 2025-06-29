# Generated by Django 5.2.2 on 2025-06-11 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
        ('profissionais', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leito',
            name='profissional',
        ),
        migrations.RemoveField(
            model_name='leito',
            name='tipoLeito',
        ),
        migrations.AddField(
            model_name='leito',
            name='tipo_leito',
            field=models.CharField(choices=[('Enfermaria', 'Enfermaria'), ('UTI', 'UTI'), ('Isolamento', 'Isolamento')], default='Enfermaria', max_length=20),
        ),
        migrations.AlterField(
            model_name='leito',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leitos', to='pacientes.paciente'),
        ),
        migrations.AlterField(
            model_name='leito',
            name='status',
            field=models.CharField(choices=[('Disponível', 'Disponível'), ('Ocupado', 'Ocupado'), ('Manutenção', 'Manutenção')], default='Disponível', max_length=20),
        ),
        migrations.AlterModelTable(
            name='leito',
            table=None,
        ),
    ]
