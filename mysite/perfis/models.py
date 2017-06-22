from django.db import models

# Create your models here.
class Perfil(object):
    """docstring for Perfil ."""
    def __init__(self, nome='', email='', fone='', empresa=''):
        super(Perfil , self).__init__()
        self.nome = nome
        self.email = email
        self.fone = fone
        self.empresa = empresa
        
