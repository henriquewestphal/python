from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil

# Create your views here.
class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        print("teste1")

        if form.is_valid():
            dados_form = form.data
            print("teste5")
            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

            perfil = Perfil(nome=dados_form['nome'],
                            fone=dados_form['telefone'],
                            empresa=dados_form['empresa'],
                            usuario=usuario)
            perfil.save()
            print("teste5")
            return redirect('index')
        print("teste6")
        return render(request, self.template_name, {'form' : form })
