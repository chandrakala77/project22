from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chandhu(request,data):
    return HttpResponse(f'hello {data}')