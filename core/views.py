from django.shortcuts import render
from django.views import View
from .utils import get_movies_from_api, get_movie_details


class ListMoviesView(View):
 
    def get(self, request, *args, **kwargs):
        
        search =""
        title_h1 ="Popular Movies" #Text that will be displayed in the main title

        #Verify that was made a search request
        if request.GET.get('search'):
            search = request.GET.get('search')
            title_h1 =f"Results found: {search}"
        #Get the movies
        movies = get_movies_from_api(search)
        
        return render(request, 'index.html', context={'movies': movies, 'title_h1': title_h1})

class DetailsMovieView(View):

    def get(self, request, *args, **kwargs):

        #Get the movie by id
        movie = get_movie_details(self.kwargs['id'])
              
        context={'movie': movie}
           
        return render(request, 'details.html', context)
    