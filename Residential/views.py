# -*- coding:UTF-8 -*-
from django.shortcuts import render_to_response

__author__ = 'jotage'


def home(request):
    return render_to_response('home.html')