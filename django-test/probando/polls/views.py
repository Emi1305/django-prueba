from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello worls. This is the polls index')

def detail(request, question_id):
    return HttpResponse