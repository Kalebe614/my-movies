from django.shortcuts import render
from django.views import View
from .utils import get_movies_from_api, get_movie_details


class ListMoviesView(View):
 
    def get(self, request, *args, **kwargs):
        
        movies = get_movies_from_api()
        
        return render(request, 'index.html', context={'movies': movies})

class DetailsMovieView(View):

    def get(self, request, *args, **kwargs):

        movie = get_movie_details(self.kwargs['id'])
        print(movie)       
        context={'movie': movie}
           
        return render(request, 'details.html', context)
    