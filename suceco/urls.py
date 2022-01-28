from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
#from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    path('', include('registros.urls')),
    path('especies/', include('especies.urls')),
    path('formacaoflorestal/', include('formacaoflorestal.urls')),
    path('registros/', include('registros.urls')),
    path('contato/', include('contato.urls')),
]
