from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='reg_index'),
    path('search/', views.search, name='search_regs_by_sp'),
    path('edit/(?P<id>\d+)$/', views.edit, name='edit_register'),
    path('create/', views.create, name='create_register'),
    path('delete/(?P<id>\d+)$/', views.delete, name='delete_register'),
    path('csv/', views.export_csv, name='generate_csv')
]
