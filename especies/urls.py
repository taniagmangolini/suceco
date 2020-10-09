from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('teste/', views.teste, name='teste'),
  #  path('detail/(?P<pk>\d+)$/', views.EspecieDetailView.as_view(), name='detail'),
    path('edit/(?P<id>\d+)$/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('delete/(?P<id>\d+)$/', views.delete, name='delete')
]
