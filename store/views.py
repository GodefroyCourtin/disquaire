# from django.shortcuts import render

from django.http import HttpResponse

from .models import Artist, Album, Contact, Booking

from django.template import loader

# Create your views here.



def index(request):
    albums = Album.objects.filter(available=True).order_by("-created_at")[:3]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    template = loader.get_template('store/index.html')
    context = {
        'albums': albums
    }
    return HttpResponse(template.render(context, request=request))
    
    
    


def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()]) # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    if not albums.exists():
        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    else:
        albums = ["<li>{}</li>".format(album.title) for album in albums]
        message = """
            
            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            
            <ul>{}</ul>
        """.format("</li><li>".join(albums))

    return HttpResponse(message)