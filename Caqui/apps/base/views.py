"""Views for the base app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def iq(request):
    return render(request, 'base/instituto/iq.html')

def imecc(request):
    return render(request, 'base/instituto/imecc.html')

def ifgw(request):
    return render(request, 'base/instituto/ifgw.html')

def ifch(request):
    return render(request, 'base/instituto/ifch.html')

def feagri(request):
    return render(request, 'base/instituto/feagri.html')

def iel(request):
    return render(request, 'base/instituto/iel.html')

def ic(request):
    return render(request, 'base/instituto/ic.html')

def ib(request):
    return render(request, 'base/instituto/ib.html')

def ig(request):
    return render(request, 'base/instituto/ig.html')

def feq(request):
    return render(request, 'base/instituto/feq.html')

def fenf(request):
    return render(request, 'base/instituto/fenf.html')

def fem(request):
    return render(request, 'base/instituto/fem.html')

def feec(request):
    return render(request, 'base/instituto/feec.html')

def feagri(request):
    return render(request, 'base/instituto/feagri.html')

def fea(request):
    return render(request, 'base/instituto/fea.html')

def fcm(request):
    return render(request, 'base/instituto/fcm.html')

def dados(request):
    return render(request, 'base/instituto/dados.html')
