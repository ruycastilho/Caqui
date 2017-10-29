"""Base models"""

from django.db import models

class Instituto(object):
    class Meta:
        db_table = 'Instituto'

    id_instituto = models.IntegerField(db_column='ID_Instituto')
    nome = models.CharField(db_column='Nome')
    sigla = models.CharField(db_column='Sigla')
    campus = models.CharField(db_column='Campus')

class Gasto_Instituto(object):
    class Meta:
        db_table = 'Gasto_Instituto'

    id_instituto = models.IntegerField(db_column='ID_Instituto')
    receita_total = models.DecimalField(db_column='Receita_Total', decimal_places=2)
    despesa_total = models.DecimalField(db_column='Despesa_Total', decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    ID = models.IntegerField(db_column='ID')

class Auxilio_Estudantil(object):
    class Meta:
        db_table = 'Auxilio_Estudantil'

    ID = models.IntegerField(db_column='ID')
    descricao = models.CharField(db_column='Descricao')
    receita_total = models.DecimalField(db_column='Receita', decimal_places=2)
    despesa_total = models.DecimalField(db_column='Despesa', decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    ID = models.IntegerField(db_column='ID_Instituto')

class Correios(object):
    class Meta:
        db_table = 'Correios'

    ID = models.IntegerField(db_column='ID')
    descricao = models.CharField(db_column='Descricao')
    receita_total = models.DecimalField(db_column='Receita', decimal_places=2)
    despesa_total = models.DecimalField(db_column='Despesa', decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    ID = models.IntegerField(db_column='ID_Instituto')

class Despesas_Centralizadas(object):
    class Meta:
        db_table = 'Despesas_Centralizadas'

    ID = models.IntegerField(db_column='ID')
    descricao = models.CharField(db_column='Descricao')
    receita_total = models.DecimalField(db_column='Receita', decimal_places=2)
    despesa_total = models.DecimalField(db_column='Despesa', decimal_places=2)
    ano = models.IntegerField(db_column='Ano')
    ID = models.IntegerField(db_column='ID_Instituto')

class Energia_Eletrica(object):
	class Meta:
		db_table = 'Energia_Eletrica'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Estagiarios(object):
	class Meta:
		db_table = 'Estagiarios'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Obras_e_Instalacoes(object):
	class Meta:
		db_table = 'Obras_e_Instalacoes'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Pessoal_e_Reflexos(object):
	class Meta:
		db_table = 'Pessoal_e_Reflexos'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Royalties(object):
	class Meta:
		db_table = 'Royalties'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Servico_de_Limpeza(object):
	class Meta:
		db_table = 'Servico_de_Limpeza'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Telefone(object):
	class Meta:
		db_table = 'Telefone'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')

class Transporte(object):
	class Meta:
		db_table = 'Transporte'

	ID = models.IntegerField(db_column='ID')
	descricao = models.CharField(db_column='Descricao')
	receita = models.DecimalField(db_column='Receita', decimal_places = 2)
	despesa = models.DecimalField(db_column='Despesa', decimal_places = 2)
	ano = models.IntegerField(db_column='Ano')
	id_instituicao = models.IntegerField(db_column='ID_Instituto')
