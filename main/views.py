from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return render(requests, 'main/index.html')

def about(requests):
    return render(requests, 'main/about.html')

def contacts(requests):
    return render(requests, 'main/contacts.html')
