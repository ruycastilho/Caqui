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

    query_data = {}

    imecc_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=3).receita
    ig_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=6).receita
    fea_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=9).receita
    iel_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=10).receita
    ib_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=12).receita
    feq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=13).receita
    feec_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=15).receita
    fem_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=16).receita
    iq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=17).receita
    ic_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/auxilio.html', query_data)

def biblioteca(request):
    '''
    query_data = {}

    imecc_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=3).receita
    ig_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=6).receita
    fea_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=9).receita
    iel_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=10).receita
    ib_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=12).receita
    feq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=13).receita
    feec_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=15).receita
    fem_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=16).receita
    iq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=17).receita
    ic_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/biblioteca.html', query_data)
    '''
    return render(request, 'base/area/biblioteca.html')


def centralizadas(request):

    query_data = {}

    imecc_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=3).receita
    ig_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=6).receita
    fea_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=9).receita
    iel_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=10).receita
    ib_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=12).receita
    feq_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=13).receita
    feec_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=15).receita
    fem_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=16).receita
    iq_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Despesas_Centralizadas.objects.all().get(id_instituicao=17).receita
    ic_despesa = Despesas_Centralizadas.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/centralizadas.html', query_data)

def correios(request):

    query_data = {}

    imecc_receita = Correios.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Correios.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Correios.objects.all().get(id_instituicao=3).receita
    ig_despesa = Correios.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Correios.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Correios.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Correios.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Correios.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Correios.objects.all().get(id_instituicao=6).receita
    fea_despesa = Correios.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Correios.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Correios.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Correios.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Correios.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Correios.objects.all().get(id_instituicao=9).receita
    iel_despesa = Correios.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Correios.objects.all().get(id_instituicao=10).receita
    ib_despesa = Correios.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Correios.objects.all().get(id_instituicao=12).receita
    feq_despesa = Correios.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Correios.objects.all().get(id_instituicao=13).receita
    feec_despesa = Correios.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Correios.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Correios.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Correios.objects.all().get(id_instituicao=15).receita
    fem_despesa = Correios.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Correios.objects.all().get(id_instituicao=16).receita
    iq_despesa = Correios.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Correios.objects.all().get(id_instituicao=17).receita
    ic_despesa = Correios.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/correios.html', query_data)

def despesas(request):
    '''
    query_data = {}

    imecc_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=3).receita
    ig_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=6).receita
    fea_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=9).receita
    iel_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=10).receita
    ib_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=12).receita
    feq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=13).receita
    feec_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=15).receita
    fem_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=16).receita
    iq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=17).receita
    ic_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/despesas.html', query_data)
    ''' 
    return render(request, 'base/area/despesas.html')


def energia(request):

    query_data = {}

    imecc_receita = Energia_Eletrica.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Energia_Eletrica.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Energia_Eletrica.objects.all().get(id_instituicao=3).receita
    ig_despesa = Energia_Eletrica.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Energia_Eletrica.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Energia_Eletrica.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Energia_Eletrica.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Energia_Eletrica.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Energia_Eletrica.objects.all().get(id_instituicao=6).receita
    fea_despesa = Energia_Eletrica.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Energia_Eletrica.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Energia_Eletrica.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Energia_Eletrica.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Energia_Eletrica.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Energia_Eletrica.objects.all().get(id_instituicao=9).receita
    iel_despesa = Energia_Eletrica.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Energia_Eletrica.objects.all().get(id_instituicao=10).receita
    ib_despesa = Energia_Eletrica.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Energia_Eletrica.objects.all().get(id_instituicao=12).receita
    feq_despesa = Energia_Eletrica.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Energia_Eletrica.objects.all().get(id_instituicao=13).receita
    feec_despesa = Energia_Eletrica.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Energia_Eletrica.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Energia_Eletrica.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Energia_Eletrica.objects.all().get(id_instituicao=15).receita
    fem_despesa = Energia_Eletrica.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Energia_Eletrica.objects.all().get(id_instituicao=16).receita
    iq_despesa = Energia_Eletrica.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Energia_Eletrica.objects.all().get(id_instituicao=17).receita
    ic_despesa = Energia_Eletrica.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/energia.html', query_data)

def estagiarios(request):

    query_data = {}

    imecc_receita = Estagiarios.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Estagiarios.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Estagiarios.objects.all().get(id_instituicao=3).receita
    ig_despesa = Estagiarios.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Estagiarios.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Estagiarios.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Estagiarios.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Estagiarios.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Estagiarios.objects.all().get(id_instituicao=6).receita
    fea_despesa = Estagiarios.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Estagiarios.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Estagiarios.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Estagiarios.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Estagiarios.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Estagiarios.objects.all().get(id_instituicao=9).receita
    iel_despesa = Estagiarios.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Estagiarios.objects.all().get(id_instituicao=10).receita
    ib_despesa = Estagiarios.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Estagiarios.objects.all().get(id_instituicao=12).receita
    feq_despesa = Estagiarios.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Estagiarios.objects.all().get(id_instituicao=13).receita
    feec_despesa = Estagiarios.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Estagiarios.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Estagiarios.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Estagiarios.objects.all().get(id_instituicao=15).receita
    fem_despesa = Estagiarios.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Estagiarios.objects.all().get(id_instituicao=16).receita
    iq_despesa = Estagiarios.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Estagiarios.objects.all().get(id_instituicao=17).receita
    ic_despesa = Estagiarios.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa}) 

    return render(request, 'base/area/estagiarios.html', query_data)

def obras(request):

    query_data = {}

    imecc_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=3).receita
    ig_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=6).receita
    fea_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=9).receita
    iel_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=10).receita
    ib_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=12).receita
    feq_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=13).receita
    feec_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=15).receita
    fem_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=16).receita
    iq_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Obras_e_Instalacoes.objects.all().get(id_instituicao=17).receita
    ic_despesa = Obras_e_Instalacoes.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/obras.html', query_data)

def pessoal(request):

    query_data = {}

    imecc_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=3).receita
    ig_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=6).receita
    fea_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=9).receita
    iel_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=10).receita
    ib_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=12).receita
    feq_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=13).receita
    feec_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=15).receita
    fem_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=16).receita
    iq_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Pessoal_e_Reflexos.objects.all().get(id_instituicao=17).receita
    ic_despesa = Pessoal_e_Reflexos.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/pessoal.html', query_data)

def servicos(request):

    query_data = {}

    imecc_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=3).receita
    ig_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=6).receita
    fea_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=9).receita
    iel_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=10).receita
    ib_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=12).receita
    feq_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=13).receita
    feec_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=15).receita
    fem_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=16).receita
    iq_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Servico_de_Limpeza.objects.all().get(id_instituicao=17).receita
    ic_despesa = Servico_de_Limpeza.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/servicos.html', query_data)

def telefone(request):

    query_data = {}
    imecc_receita = Telefone.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Telefone.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Telefone.objects.all().get(id_instituicao=3).receita
    ig_despesa = Telefone.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Telefone.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Telefone.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Telefone.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Telefone.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Telefone.objects.all().get(id_instituicao=6).receita
    fea_despesa = Telefone.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Telefone.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Telefone.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Telefone.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Telefone.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Telefone.objects.all().get(id_instituicao=9).receita
    iel_despesa = Telefone.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Telefone.objects.all().get(id_instituicao=10).receita
    ib_despesa = Telefone.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Telefone.objects.all().get(id_instituicao=12).receita
    feq_despesa = Telefone.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Telefone.objects.all().get(id_instituicao=13).receita
    feec_despesa = Telefone.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Telefone.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Telefone.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Telefone.objects.all().get(id_instituicao=15).receita
    fem_despesa = Telefone.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Telefone.objects.all().get(id_instituicao=16).receita
    iq_despesa = Telefone.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Telefone.objects.all().get(id_instituicao=17).receita
    ic_despesa = Telefone.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/telefone.html', query_data)

def transporte(request):

    query_data = {}

    imecc_receita = Transporte.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Transporte.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Transporte.objects.all().get(id_instituicao=3).receita
    ig_despesa = Transporte.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Transporte.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Transporte.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Transporte.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Transporte.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Transporte.objects.all().get(id_instituicao=6).receita
    fea_despesa = Transporte.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Transporte.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Transporte.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Transporte.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Transporte.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Transporte.objects.all().get(id_instituicao=9).receita
    iel_despesa = Transporte.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Transporte.objects.all().get(id_instituicao=10).receita
    ib_despesa = Transporte.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Transporte.objects.all().get(id_instituicao=12).receita
    feq_despesa = Transporte.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Transporte.objects.all().get(id_instituicao=13).receita
    feec_despesa = Transporte.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Transporte.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Transporte.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Transporte.objects.all().get(id_instituicao=15).receita
    fem_despesa = Transporte.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Transporte.objects.all().get(id_instituicao=16).receita
    iq_despesa = Transporte.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Transporte.objects.all().get(id_instituicao=17).receita
    ic_despesa = Transporte.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/transporte.html', query_data)

def upa(request):
    '''
    query_data = {}

    imecc_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=2).receita
    imecc_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=2).despesa
    query_data.update({'imecc_receita':imecc_receita, 'imecc_despesa':imecc_despesa})

    ig_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=3).receita
    ig_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=3).despesa
    query_data.update({'ig_receita':ig_receita, 'ig_despesa':ig_despesa})

    fcm_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=4).receita
    fcm_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=4).despesa
    query_data.update({'fcm_receita':fcm_receita, 'fcm_despesa':fcm_despesa})

    ifgw_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=5).receita
    ifgw_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=5).despesa
    query_data.update({'ifgw_receita':ifgw_receita, 'ifgw_despesa':ifgw_despesa})

    fea_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=6).receita
    fea_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=6).despesa
    query_data.update({'fea_receita':fea_receita, 'fea_despesa':fea_despesa})

    ifch_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=7).receita
    ifch_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=7).despesa
    query_data.update({'ifch_receita':ifch_receita, 'ifch_despesa':ifch_despesa})

    feagri_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=8).receita
    feagri_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=8).despesa
    query_data.update({'feagri_receita':feagri_receita, 'feagri_despesa':feagri_despesa})

    iel_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=9).receita
    iel_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=9).despesa
    query_data.update({'iel_receita':iel_receita, 'iel_despesa':iel_despesa})

    ib_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=10).receita
    ib_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=10).despesa
    query_data.update({'ib_receita':ib_receita, 'ib_despesa':ib_despesa})

    feq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=12).receita
    feq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=12).despesa
    query_data.update({'feq_receita':feq_receita, 'feq_despesa':feq_despesa})

    feec_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=13).receita
    feec_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=13).despesa
    query_data.update({'feec_receita':feec_receita, 'feec_despesa':feec_despesa})

    fenf_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=14).receita
    fenf_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=14).despesa
    query_data.update({'fenf_receita':fenf_receita, 'fenf_despesa':fenf_despesa})

    fem_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=15).receita
    fem_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=15).despesa
    query_data.update({'fem_receita':fem_receita, 'fem_despesa':fem_despesa})

    iq_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=16).receita
    iq_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=16).despesa
    query_data.update({'iq_receita':iq_receita, 'iq_despesa':iq_despesa})

    ic_receita = Auxilio_Estudantil.objects.all().get(id_instituicao=17).receita
    ic_despesa = Auxilio_Estudantil.objects.all().get(id_instituicao=17).despesa
    query_data.update({'ic_receita':ic_receita, 'ic_despesa':ic_despesa})

    return render(request, 'base/area/upa.html', query_data))
    '''

    return render(request, 'base/area/upa.html')
