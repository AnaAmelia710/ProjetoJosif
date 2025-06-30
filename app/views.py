from django.shortcuts import render
from .models import Pessoa, PontoColeta, TipoResiduo, CampanhaColeta, ParticipacaoCampanha, HistoricoDescartes
#cadastro
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#requerimento login
from django.contrib.auth.decorators import login_required

def pagina_inicial(request):
    return render(request, 'index.html')

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

def lista_historico(request):
    historicos = HistoricoDescartes.objects.all()
    return render(request, 'historico.html', {'historicos': historicos})


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
