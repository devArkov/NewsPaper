from django.urls import path

from . import views


app_name = 'public'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
]