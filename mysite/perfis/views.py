from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == "1":
        perfil = Perfil('Henrique Westphal', 'henriquewalves@gmail.com','999999999','linux')

    if perfil_id == "2":
        perfil = Perfil('Suelyn de Assis', 'suelyndeassis@gmail.com','999999988','udo')

    print ('id do perfil %s ' % perfil_id)
    return render(request, 'perfils.html', { "perfil" : perfil})
