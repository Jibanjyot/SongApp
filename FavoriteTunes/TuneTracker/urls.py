from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.song_list, name='song_list'),
    path('song/<int:song_id>/', views.song_details, name='song_details'),
    path('add/song', views.add_song, name='add_song'),
    path('add/artist', views.add_artist, name='add_artist'),
    path('artist/<int:artist_id>/', views.artist_details, name='artist_details'),
]