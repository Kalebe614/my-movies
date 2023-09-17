from django.shortcuts import render
from django.views import View
from .utils import get_movies_from_api


class ListMoviesView(View):
 
    def get(self, request, *args, **kwargs):
        
        movies = get_movies_from_api()
        
        return render(request, 'index.html', context={'movies': movies})