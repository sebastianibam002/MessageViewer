from http.client import HTTPResponse
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django import forms
from .models import StateOfDevice
from .spotify_retrieve import get_random_song_from_playlist

# Create your views here.



def index(request):

         # Check if method is POST
        if request.method == "POST":
                # Take in the data the user submitted and save it as form
                message = request.POST['message']
                rgb_one = request.POST['rgb_one']
                rgb_two = request.POST['rgb_two']
                rgb_three = request.POST['rgb_three']
                rgb_four = request.POST['rgb_four']
                # I have to upload it into the database and make it available
                # in another app in case someone wants to check it
                StateOfDevice.objects.create(message=message, 
                led_one_hex=rgb_one, led_two_hex=rgb_two, 
                led_three_hex=rgb_three, led_four_hex=rgb_four)
        current_time = datetime.datetime.now().hour
        tiempo = ""
        if current_time >= 0 and current_time < 12:
                tiempo = "morning"
        elif current_time >= 12 and current_time < 18:
                tiempo = "evening"
        else:
                tiempo = "night"

        dic_info_spotify = get_random_song_from_playlist()
        print(dic_info_spotify)
        return render(request, "home/index.html", {
                "time_of_day": tiempo.title(),
                "name_song": dic_info_spotify["name_song"],
                "artist": dic_info_spotify["artist_name"],
                "image_song": dic_info_spotify['image_url'],
                "preview_song": dic_info_spotify['preview_url'],

        })
