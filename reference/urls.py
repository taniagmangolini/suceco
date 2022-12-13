from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReferenceView.as_view(), name='index'),
    path('edit/(?P<id>\d+)$/', views.edit, name='edit_reference'),
    path('create/', views.create, name='create_reference'),
    path('delete/(?P<id>\d+)$/', views.delete, name='delete_reference'),
]
