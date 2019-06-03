from django.shortcuts import render
from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'musicas/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Esse album não foi encontrado no banco de dados")
    return render(request, "musicas/detail.html", {'album': album})

