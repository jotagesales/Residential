# -*- coding:UTF-8 -*-
from django.shortcuts import render_to_response

__author__ = 'jotage'


def home(request):
    return render_to_response('home.html')


def sobre(request):
    return render_to_response('sobre.html')


def cadastro(request):
    return render_to_response('cadastro.html')


def contato(request):
    return render_to_response('contato.html')


def portfolio(request):
    return render_to_response('portfolio.html')


def servicos(request):
    return render_to_response('servicos.html')