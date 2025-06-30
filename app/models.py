from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    disponibilidade = models.CharField(max_length=100, verbose_name="Disponibilidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupacao"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"

class TipoResiduo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do resíduo")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "TipoResíduo"

class PontoColeta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do ponto")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ponto_referencia = models.CharField(max_length=200, verbose_name="Ponto de referência")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "PontoColeta"

class ResiduoDescartado(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    tipo_residuo = models.ForeignKey(TipoResiduo, on_delete=models.CASCADE, verbose_name="Tipo de Resíduo")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    data_descarte = models.DateField(verbose_name="Data do Descarte")
    ponto_coleta = models.ForeignKey(PontoColeta, on_delete=models.CASCADE, verbose_name="PontoColeta")

    def __str__(self):
        return f"{self.pessoa} - {self.tipo_residuo} ({self.quantidade})"

    class Meta:
        verbose_name = "ResíduoDescartado"


class CampanhaColeta(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da campanha")
    descricao = models.TextField(verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "CampanhaColeta"

class ParticipacaoCampanha(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    campanha = models.ForeignKey(CampanhaColeta, on_delete=models.CASCADE, verbose_name="Campanha")
    quantidade_residuos_descartados = models.IntegerField(verbose_name="Quantidade de Resíduos Descartados")

    def __str__(self):
        return f"{self.pessoa} em {self.campanha}"

    class Meta:
        verbose_name = "ParticipacaoCampanha"


class HistoricoDescartes(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    residuo_descartado = models.ForeignKey(ResiduoDescartado, on_delete=models.CASCADE, verbose_name="Resíduo Descartado")
    data_registro = models.DateField(verbose_name="Data de Registro")
    quantidade = models.IntegerField(verbose_name="Quantidade")

    def __str__(self):
        return f"{self.pessoa} - {self.residuo_descartado} ({self.quantidade})"

    class Meta:
        verbose_name = "HistóricoDescarte"

