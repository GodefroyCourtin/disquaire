
from django.conf.urls import url 
from . import views  # importer toutes les les vues de notre applications

urlpatterns = [            
    url(r"^$", views.listing), # toute urls qui commencent ou finit par une chaine vide est relié à la vue index. 
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),  # /store/2 ou /store/12 par exemple
    url(r"^search/$", views.search),
] 