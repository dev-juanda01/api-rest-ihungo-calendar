from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='Correo', blank=True, unique=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )
    identification = models.CharField(
        verbose_name='Numero de Identificacion', max_length=15, unique=True, null=False, blank=False)
    city = models.CharField(verbose_name='Ciudad', max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()


class NotificationForUser(models.Model):
    message = models.TextField(verbose_name='Notificaciones')
    date_created = models.DateTimeField(
        verbose_name='Fecha de creacion', auto_now_add=True, editable=False)
    for_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'NotificationForUser'
        verbose_name_plural = 'NotificationForUsers'
        db_table = 'notification_for_user'
