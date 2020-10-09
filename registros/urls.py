from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistrosView.as_view(), name='index'),
    path('edit/(?P<id>\d+)$/', views.edit, name='edit_registro'),
    path('create/', views.create, name='create_registro'),
    path('delete/(?P<id>\d+)$/', views.delete, name='delete_registro')
]
