from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Conta(models.Model):

    nome = models.CharField(max_length=255, null=False)
    fone = models.CharField(max_length=15, null=False)
    empresa = models.CharField(max_length=255, null=False)
    saldo = models.DecimalField(max_digits=10000, decimal_places=0, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name="conta")

    @property
    def email(self):
        return self.forms.email
