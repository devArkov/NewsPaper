from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def news(request: HttpRequest) -> HttpResponse:
    return render(request, 'news.html')


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
