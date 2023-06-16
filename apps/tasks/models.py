from django.db import models
from apps.users.models import User

# Create your models here.


class Task(models.Model):
    activity_type = models.CharField(
        verbose_name='Tipo de Actividad', max_length=200, null=False)
    description = models.TextField(verbose_name='Descripción', null=True)
    start_date = models.DateTimeField(
        verbose_name='Fecha de Inicio', null=False)
    end_date = models.DateTimeField(verbose_name='Fecha de Fin', null=False)
    color = models.CharField(verbose_name='Color', max_length=10)
    user = models.ForeignKey(
        User, verbose_name='Usuario', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.activity_type}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'
