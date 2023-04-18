from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='zzz-home'),
    path('contacts/', views.contacts, name='zzz-contacts'),
    path('aegis/', views.aegis, name='zzz-aegis'),
    path('parad/', views.parad, name='zzz-parad'),
]