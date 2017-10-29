# -*- coding: utf-8 -*-
"""Views for the base app"""

from django.shortcuts import render
from .models import *

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def query(IDE):

    # receitadd
    receita_total = Gasto_Instituto.objects.all().get(id_instituicao=IDE).receita_total
    auxilio = Auxilio_Estudantil.objects.all().get(id_instituicao=IDE).receita
    correios = Correios.objects.all().get(id_instituicao=IDE).receita
    despesas = Despesas_Centralizadas.objects.all().get(id_instituicao=IDE).receita
    energia = Energia_Eletrica.objects.all().get(id_instituicao=IDE).receita
    estagiarios = Estagiarios.objects.all().get(id_instituicao=IDE).receita
    obras = Obras_e_Instalacoes.objects.all().get(id_instituicao=IDE).receita
    pessoal = Pessoal_e_Reflexos.objects.all().get(id_instituicao=IDE).receita
    royalties = Royalties.objects.all().get(id_instituicao=IDE).receita
    limpeza = Servico_de_Limpeza.objects.all().get(id_instituicao=IDE).receita
    telefone = Telefone.objects.all().get(id_instituicao=IDE).receita
    transporte = Transporte.objects.all().get(id_instituicao=IDE).receita
    
    query_data = {'receita_total': receita_total, 'auxilio': auxilio, 'correios': correios, 'despesas': despesas, 'energia': energia, 'estagiarios': estagiarios, 'obras': obras, 'pessoal': pessoal, 'royalties': royalties, 'limpeza': limpeza, 'telefone': telefone, 'transporte': transporte}

    # despesa
    receita_total = Gasto_Instituto.objects.all().get(id_instituicao=IDE).despesa_total
    auxilio = Auxilio_Estudantil.objects.all().get(id_instituicao=IDE).despesa
    correios = Correios.objects.all().get(id_instituicao=IDE).despesa
    despesas = Despesas_Centralizadas.objects.all().get(id_instituicao=IDE).despesa
    energia = Energia_Eletrica.objects.all().get(id_instituicao=IDE).despesa
    estagiarios = Estagiarios.objects.all().get(id_instituicao=IDE).despesa
    obras = Obras_e_Instalacoes.objects.all().get(id_instituicao=IDE).despesa
    pessoal = Pessoal_e_Reflexos.objects.all().get(id_instituicao=IDE).despesa
    royalties = Royalties.objects.all().get(id_instituicao=IDE).despesa
    servico = Servico_de_Limpeza.objects.all().get(id_instituicao=IDE).despesa
    telefone = Telefone.objects.all().get(id_instituicao=IDE).despesa
    transporte = Transporte.objects.all().get(id_instituicao=IDE).despesa

    aux = {'receita_total_despesa': receita_total, 'auxilio_despesa': auxilio, 'correios_despesa': correios, 'despesas_despesa': despesas, 'energia_despesa_despesa': energia, 'estagiarios_despesa': estagiarios, 'obras_despesa': obras, 'pessoal_despesa': pessoal, 'royalties_despesa': royalties, 'limpeza_despesa': limpeza, 'telefone_despesa': telefone, 'transporte_despesa': transporte}

    query_data.update(aux)

    return query_data

def megaPrint(IDE):
    # receita
    print(Gasto_Instituto.objects.all().get(id_instituicao=IDE).receita_total)
    print(Auxilio_Estudantil.objects.all().get(id_instituicao=IDE).receita)
    print(Correios.objects.all().get(id_instituicao=IDE).receita)
    print(Despesas_Centralizadas.objects.all().get(id_instituicao=IDE).receita)
    print(Energia_Eletrica.objects.all().get(id_instituicao=IDE).receita)
    print(Estagiarios.objects.all().get(id_instituicao=IDE).receita)
    print(Obras_e_Instalacoes.objects.all().get(id_instituicao=IDE).receita)
    print(Pessoal_e_Reflexos.objects.all().get(id_instituicao=IDE).receita)
    print(Royalties.objects.all().get(id_instituicao=IDE).receita)
    print(Servico_de_Limpeza.objects.all().get(id_instituicao=IDE).receita)
    print(Telefone.objects.all().get(id_instituicao=IDE).receita)
    print(Transporte.objects.all().get(id_instituicao=IDE).receita)
    
    print('\n')
    # despesa
    print(Gasto_Instituto.objects.all().get(id_instituicao=IDE).despesa_total)
    print(Auxilio_Estudantil.objects.all().get(id_instituicao=IDE).despesa)
    print(Correios.objects.all().get(id_instituicao=IDE).despesa)
    print(Despesas_Centralizadas.objects.all().get(id_instituicao=IDE).despesa)
    print(Energia_Eletrica.objects.all().get(id_instituicao=IDE).despesa)
    print(Estagiarios.objects.all().get(id_instituicao=IDE).despesa)
    print(Obras_e_Instalacoes.objects.all().get(id_instituicao=IDE).despesa)
    print(Pessoal_e_Reflexos.objects.all().get(id_instituicao=IDE).despesa)
    print(Royalties.objects.all().get(id_instituicao=IDE).despesa)
    print(Servico_de_Limpeza.objects.all().get(id_instituicao=IDE).despesa)
    print(Telefone.objects.all().get(id_instituicao=IDE).despesa)
    print(Transporte.objects.all().get(id_instituicao=IDE).despesa)
    
    print('\n')


    return

def iq(request):
    inst = Instituto.objects.all().filter(nome='Instituto de Química')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/iq.html', query(IDE))


def imecc(request):
    
    inst = Instituto.objects.all().filter(nome='Instituto de Matemática Estástica e Computação Científica')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/imecc.html', query(IDE))


def ifgw(request):

    inst = Instituto.objects.all().filter(nome='Instituto de Física \"Gleb Wataghin\"')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto


    return render(request, 'base/instituto/ifgw.html', query(IDE))

def ifch(request):

    inst = Instituto.objects.all().filter(nome='Instituto de Filosofia e de Ciências Humanas')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/ifch.html', query(IDE))


def feagri(request):

    inst = Instituto.objects.all().filter(nome='Faculdade de engenharia agrícola')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/feagri.html', query(IDE))


def iel(request):

    inst = Instituto.objects.all().filter(nome='Instituto de Estudos da Linguagem')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/iel.html', query(IDE))


def ic(request):

    inst = Instituto.objects.all().filter(nome='Instituto de Computação')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/ic.html', query(IDE))


def ib(request):
    inst = Instituto.objects.all().filter(nome='Instituto de Biologia')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto
    return render(request, 'base/instituto/ib.html', query(IDE))


def ig(request):

    inst = Instituto.objects.all().filter(nome='Instituto de Geociências')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto


    return render(request, 'base/instituto/ig.html', query(IDE))


def feq(request):

    inst = Instituto.objects.all().filter(nome='Faculdade de Engenharia Química')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/feq.html', query(IDE))


def fenf(request):

    inst = Instituto.objects.all().filter(nome='Faculdade de Enfermagem')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto


    return render(request, 'base/instituto/fenf.html', query(IDE))


def fem(request):

    inst = Instituto.objects.all().filter(nome='Faculdade de Engenharia Mecânica')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto


    return render(request, 'base/instituto/fem.html', query(IDE))


def feec(request):

    inst = Instituto.objects.all().filter(nome='Faculdade de Engenharia Elétrica e Computação')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/feec.html', query(IDE))


def fea(request):

    inst = Instituto.objects.all().filter(nome='Faculdade de Engenharia de Alimentos')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/fea.html', query(IDE))


def fcm(request):

    inst = Instituto.objects.all().filter(nome='Faculdade Ciências Médicas')
    for instituto in inst:
        print(instituto.nome)
        IDE = instituto.id_instituto

    return render(request, 'base/instituto/fcm.html', query(IDE))


def dados(request):
    return render(request, 'base/instituto/dados.html')

#-------------------------
def auxilio(request):
    return render(request, 'base/area/auxilio.html')

def biblioteca(request):
    return render(request, 'base/area/biblioteca.html')

def centralizadas(request):
    return render(request, 'base/area/centralizados.html')

def correios(request):
    return render(request, 'base/area/correios.html')

def despesas(request):
    return render(request, 'base/area/despesas.html')

def energia(request):
    return render(request, 'base/area/energia.html')

def estagiarios(request):
    return render(request, 'base/area/estagiarios.html')

def obras(request):
    return render(request, 'base/area/obras.html')

def pessoal(request):
    return render(request, 'base/area/pessoal.html')

def servicos(request):
    return render(request, 'base/area/servicos.html')

def telefone(request):
    return render(request, 'base/area/telefone.html')

def transporte(request):
    return render(request, 'base/area/transporte.html')

def upa(request):
    return render(request, 'base/area/upa.html')


