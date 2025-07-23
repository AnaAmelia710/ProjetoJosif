from django.shortcuts import render
from .models import Pessoa, PontoColeta, TipoResiduo, CampanhaColeta, ParticipacaoCampanha
#cadastro
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#requerimento login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def pagina_inicial(request):
    campanhas = CampanhaColeta.objects.all().order_by('-data_inicio')[:5]
    pontos = PontoColeta.objects.all()
    
    participacoes = None
    if request.user.is_authenticated:
        participacoes = ParticipacaoCampanha.objects.filter(pessoa__email=request.user.email)

    contexto = {
        'campanhas': campanhas,
        'pontos': pontos,
        'participacoes': participacoes
    }

    return render(request, 'index.html', contexto)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def lista_pontos_coleta(request):
    pontos = PontoColeta.objects.all()
    return render(request, 'pontos_coleta.html', {'pontos': pontos})
def pontos_coleta_view(request):
    pontos = PontoColeta.objects.all()
    return render(request, 'pontos_coleta.html', {'pontos': pontos})


def lista_tipos_residuos(request):
    tipos = TipoResiduo.objects.all()
    return render(request, 'tipos_residuos.html', {'tipos': tipos})

def lista_campanhas(request):
    campanhas = CampanhaColeta.objects.all()
    return render(request, 'campanhas.html', {'campanhas': campanhas})

def lista_participacoes(request):
    participacoes = ParticipacaoCampanha.objects.all()
    return render(request, 'participacoes.html', {'participacoes': participacoes})


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona para login após cadastro
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

#requerer login

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas': pessoas})
@login_required
def perfil(request):
    return render(request, 'perfil.html')
