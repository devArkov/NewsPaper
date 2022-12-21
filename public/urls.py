from django.urls import path

from . import views


app_name = 'public'
urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]