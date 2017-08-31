#!/usr/bin/env python

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def hello1(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)