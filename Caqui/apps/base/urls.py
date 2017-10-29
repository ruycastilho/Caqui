"""urlconf for the base application"""

from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^instituto/iq.html', iq, name='iq'),
    url(r'^instituto/imecc.html', imecc, name='imecc'),
    url(r'^instituto/ig.html', ig, name='ig'),
    url(r'^instituto/ifgw.html', ifgw, name='ifgw'),
    url(r'^instituto/ifch.html', ifch, name='ifch'),
    url(r'^instituto/iel.html', iel, name='iel'),
    url(r'^instituto/ic.html', ic, name='ic'),
    url(r'^instituto/ib.html', ib, name='ib'),
    url(r'^instituto/feq.html', feq, name='feq'),
    url(r'^instituto/fenf.html', fenf, name='fenf'),
    url(r'^instituto/fem.html', fem, name='fem'),
    url(r'^instituto/feec.html', feec, name='feec'),
    url(r'^instituto/feagri.html', feagri, name='feagri'),
    url(r'^instituto/fea.html', fea, name='fea'),
    url(r'^instituto/fcm.html', fcm, name='fcm'),
    url(r'^instituto/dados.html', dados, name='dados'),

	url(r'^area/auxilio.html', iq, name='auxilio'),
    url(r'^area/biblioteca.html', imecc, name='biblioteca'),
    url(r'^area/centralizadas.html', ig, name='centralizadas'),
    url(r'^area/correios.html', ifgw, name='correios'),
    url(r'^area/despesas.html', ifch, name='despesas'),
    url(r'^area/energia.html', iel, name='energia'),
    url(r'^area/estagiarios.html', ic, name='estagiarios'),
    url(r'^area/obras.html', ib, name='obras'),
    url(r'^area/pessoal.html', feq, name='pessoal'),
    url(r'^area/servicos.html', fenf, name='servicos'),
    url(r'^area/telefone.html', fem, name='telefone'),
    url(r'^area/transporte.html', feec, name='transporte'),
    url(r'^area/upa.html', feagri, name='upa'),
	
]
