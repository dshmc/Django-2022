#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request)
    return HttpResponse('<h1>Hello world</h1>')

def test(request):
    return HttpResponse('<h1> Тестова сторінка </h1>')

def first_test(request):
    return HttpResponse('<h3>Я майбутній Джанго розробник.</h33>')