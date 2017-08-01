from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from banco_hipster.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from banco_hipster.models import Conta

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

            conta = Conta(nome=dados_form['nome'],
                            fone=dados_form['telefone'],
                            empresa=dados_form['empresa'],
                            saldo=dados_form['saldo'],
                            usuario=usuario)
            conta.save()
            print("teste6")
            return redirect('index')
        print("teste7")
        return render(request, self.template_name, {'form' : form })



#@login_required
def index(request):
    return render(request, 'index.html', {'contas' : Conta.objects.all(),
        'conta_logado' :  get_conta_logado(request)})

#@login_required
def exibir(request, perfil_id):

    conta = Conta.objects.get(id=conta_id)
    conta_logado = get_conta_logado(request)
    ja_eh_contato =  conta in conta_logado.contatos.all()
    return render(request, 'contas.html', { "conta" : conta, 'ja_eh_contato' : ja_eh_contato})

#@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

#@login_required
def aceitar(request, convite_id):
    convite= Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

#@login_required
def get_conta_logado(request):
    return request.user.conta
