from django.urls import path
from . import views

urlpatterns = [
    path('', views.SpeciesView.as_view(), name='index'),
    path('edit/(?P<id>\d+)$/', views.edit, name='edit_species'),
    path('create/', views.create, name='create_species'),
    path('delete/(?P<id>\d+)$/', views.delete, name='delete_species')
]
