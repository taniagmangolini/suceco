from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    path('', include('register.urls')),
    path('species/', include('species.urls')),
    path('forest/', include('forest.urls')),
    path('reference/', include('reference.urls')),
    path('register/', include('register.urls')),
    path('contact/', include('contact.urls')),
]

