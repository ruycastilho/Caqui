"""Base models"""

from django.db import models

class Instituto(models.Model):
    class Meta:
        db_table = 'Instituto'

    id_instituto = models.IntegerField(db_column='ID_Instituto', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=75)
    sigla = models.CharField(db_column='Sigla', max_length=10)
    campus = models.CharField(db_column='Campus', max_length=20)

class Gasto_Instituto(models.Model):
    class Meta:
        db_table = 'Gasto_Instituto'

    id_instituicao = models.IntegerField(db_column='ID_Instituto')
    receita_total = models.DecimalField(db_column='Receita_Total', max_digits=13, decimal_places=2)
    despesa_total = models.DecimalField(db_column='Despesa_Total', max_digits=13, decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    ID = models.IntegerField(db_column='ID', primary_key=True)

class Auxilio_Estudantil(models.Model):
    class Meta:
        db_table = 'Auxilio_Estudantil'

    ID = models.IntegerField(db_column='ID', primary_key=True)
    descricao = models.CharField(db_column='Descricao', max_length=300)
    receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places=2)
    despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Correios(models.Model):
    class Meta:
        db_table = 'Correios'

    ID = models.IntegerField(db_column='ID', primary_key=True)
    descricao = models.CharField(db_column='Descricao', max_length=300)
    receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places=2)
    despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Despesas_Centralizadas(models.Model):
    class Meta:
        db_table = 'Despesas_Centralizadas'

    ID = models.IntegerField(db_column='ID', primary_key=True)
    descricao = models.CharField(db_column='Descricao', max_length=300)
    receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places=2)
    despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Energia_Eletrica(models.Model):
	class Meta:
		db_table = 'Energia_Eletrica'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Estagiarios(models.Model):
	class Meta:
		db_table = 'Estagiarios'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Obras_e_Instalacoes(models.Model):
	class Meta:
		db_table = 'Obras_e_Instalacoes'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Pessoal_e_Reflexos(models.Model):
	class Meta:
		db_table = 'Pessoal_e_Reflexos'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Royalties(models.Model):
	class Meta:
		db_table = 'Royalties'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Servico_de_Limpeza(models.Model):
	class Meta:
		db_table = 'Servico_de_Limpeza'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Telefone(models.Model):
	class Meta:
		db_table = 'Telefone'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Transporte(models.Model):
	class Meta:
		db_table = 'Transporte'

	ID = models.IntegerField(db_column='ID', primary_key=True)
	descricao = models.CharField(db_column='Descricao', max_length=300)
	receita = models.DecimalField(db_column='Receita', max_digits=13, decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', max_digits=13, decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')
