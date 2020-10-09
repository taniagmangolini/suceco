from django.urls import path
from . import views

urlpatterns = [
    path('', views.EspeciesView.as_view(), name='index'),
    path('edit/(?P<id>\d+)$/', views.edit, name='edit_especie'),
    path('create/', views.create, name='create_especie'),
    path('delete/(?P<id>\d+)$/', views.delete, name='delete_especie')
]
