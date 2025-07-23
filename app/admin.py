from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, TipoResiduo,
    PontoColeta, ResiduoDescartado,
    CampanhaColeta, ParticipacaoCampanha,
)

class ResiduoDescartadoInline(admin.TabularInline):
    model = ResiduoDescartado
    extra = 1

class ParticipacaoInline(admin.TabularInline):
    model = ParticipacaoCampanha
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [ResiduoDescartadoInline, ParticipacaoInline]
    list_display = ('nome', 'email', 'cidade', 'ocupacao')

class ParticipacaoCampanhaInline(admin.TabularInline):
    model = ParticipacaoCampanha
    extra = 1

@admin.register(CampanhaColeta)
class CampanhaAdmin(admin.ModelAdmin):
    inlines = [ParticipacaoCampanhaInline]
    list_display = ('nome', 'data_inicio', 'data_fim', 'cidade')

class ResiduoColetaInline(admin.TabularInline):
    model = ResiduoDescartado
    extra = 1

@admin.register(PontoColeta)
class PontoColetaAdmin(admin.ModelAdmin):
    inlines = [ResiduoColetaInline]
    list_display = ('nome', 'endereco', 'cidade')

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(TipoResiduo)
admin.site.register(ResiduoDescartado)
admin.site.register(ParticipacaoCampanha)
