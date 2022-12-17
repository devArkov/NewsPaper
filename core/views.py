from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
