
from django.urls import path
from . import views  # importer toutes les les vues de notre applications

app_name = "store"

urlpatterns = [            
    path("", views.index, name = "index"),
    path("listing", views.listing, name = "listing"), # toute urls qui commencent ou finit par une chaine vide est relié à la vue index. 
    path('detail/<int:album_id>', views.detail, name = "detail"),  # /detail/2 ou /detail/12 par exemple
    path("search/", views.search,name = "search"),
] 