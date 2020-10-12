from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.http import HttpResponse

from .models import Artist, Album, Contact, Booking

# from django.template import loader

# Create your views here.



def index(request):
    albums = Album.objects.filter(available=True).order_by("-created_at")[:3]
    context = {
        'albums': albums
    }
    return render(request, 'store/index.html', context)
    
    
    


def listing(request):
    albums_list = Album.objects.filter(available=True)
    # Slice pages
    paginator = Paginator(albums_list, 9)
    # Get current page number
    page = request.GET.get('page')
    try:
        # Return only this page albums and not others
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        albums = paginator.page(paginator.num_pages)
    context = {
        'albums': albums,
        'paginate':True
    }
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()]) # grab artists name and create a string out of it.
    context = {
        'album':album,
        'artists_name': artists_name,
    }
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    title = "Résultats pour la requête %s"%query

    context = {
        'albums': albums,
        'title': title
    }
    # if not albums.exists():
    #     message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    # else:
    #     albums = ["<li>{}</li>".format(album.title) for album in albums]
    #     message = """
            
    #         Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            
    #         <ul>{}</ul>
    #     """.format("</li><li>".join(albums))

    return render(request, 'store/search.html', context)