"""disquaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static # pour les photos
from django.contrib import admin
from django.urls import path

from store import views

urlpatterns = [
    # url(r'^$', views.index),
    path('', include('store.urls')),  #url, va directement cherhcer les url qui commencent par store/
    path("admin/", admin.site.urls),         #path, va directement dans le dossier "admin"
    
]


    # import debug_toolbar

    # urlpatterns = [
    #     url(r"^__debug__/", include(debug_toolbar.urls)),
    # ] + urlpatterns

#pour les photos

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif getattr(settings, 'FORCE_SERVE_STATIC', False):
    settings.DEBUG = True
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    settings.DEBUG = False