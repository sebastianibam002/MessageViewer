from distutils.file_util import move_file
from django.shortcuts import render
from movielist.movieRetrieve import query_search
from movielist.models import Movies
# Create your views here.
def index(request):
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        movie_title = request.POST['movie_title']
        poster_path = query_search(movie_title)[1]
        print()
        if not Movies.objects.filter(title=movie_title).exists():
            Movies.objects.create(title=movie_title, poster_image=poster_path, complete_name=movie_title.replace(" ", "+"))
    elif request.method == "GET":
        # trying to remove a movie
        movie_title = request.GET.get('remove_movie')
        Movies.objects.filter(complete_name=movie_title).delete()

    return render(request, "movielist/movies.html", {"movies": Movies.objects.all()})