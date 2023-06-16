# Generated by Django 4.2.2 on 2023-06-15 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=200, verbose_name='Tipo de Actividad')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Fin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'tasks',
            },
        ),
    ]