from django.urls import path
from . import views

urlpatterns = [
    path('', views.mandar_mensagem, name='contato'),
]
