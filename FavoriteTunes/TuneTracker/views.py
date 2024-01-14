from django.shortcuts import render, redirect
from .models import Song, Artist
from .forms import ArtistForm, SongForm

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'TuneTracker/song_list.html', {'songs': songs})

def song_details(request,song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'TuneTracker/song_detail.html', {'song': song})

def artist_details(request,artist_id):
    artist = Artist.objects.get(pk=artist_id)
    song_count = Song.objects.filter(artist=artist).count()
    return render(request, 'TuneTracker/artist_detail.html', {'artist': artist, 'song_count': song_count})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = ArtistForm()

    return render(request, 'TuneTracker/add_artist.html', {'form': form})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()

    return render(request, 'TuneTracker/add_song.html', {'form': form})