from shutil import move
from typing import Dict
import requests

"""
Given a movie title, returns the movie title and poster title
"""
def query_search(query_search: str) -> list:
    link_website = f'https://api.themoviedb.org/3/search/movie?api_key=7160051645b2ca8fe626e8ffbbd0c4d2&query={query_search.replace(" ", "+")}'
    receive = requests.get(link_website)
    number_of_results = receive.json()['total_results']
    # limit the results to 5
    if number_of_results > 5:
        number_of_results = 5
    dic_results = {}
    title_movie = receive.json()['results'][0]['original_title']
    poster_link = receive.json()['results'][0]['poster_path'] 
    poster_path = f"https://image.tmdb.org/t/p/w500/{poster_link}"
    # retrieve the complete name of the movie and the code
    return [title_movie, poster_path]

print(query_search("The Imitation Game"))