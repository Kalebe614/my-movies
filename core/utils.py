import requests
   
#Get the movies from https://developer.themoviedb.org/
def get_movies_from_api(name_movie):
       
        url = name_movie

        if url == "":
            #Popular movies
            url ="https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"   
        
        else:
            #Search for movie
            url = f"https://api.themoviedb.org/3/search/movie?query={name_movie}&include_adult=false&language=en-US&page=1"

        
        #Token read
        only_read = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjQ1MDYzZWZkMjI5MDVlZGVmYjcyNGQ1YWJmN2UxYSIsInN1YiI6IjY1MDM0OGQ5ZWZlYTdhMDBhYWQ4ZDE0MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CWd3TH07PtdOyidPWA3zv37iwan_lODThjB6d2whAXo"
        headers = {"accept": "application/json", "Authorization": f"Bearer {only_read}"}
        #Get the movies 
        response = requests.get(url, headers=headers)
       
        #Search for movies
        if (response.status_code==200):
            
            results = response.json()
            movies = results.get('results')
        else:
            movies = []
            print(response.status_code)
        return movies


def get_movie_details(movie_id):
     
     #Details about movie
        url_detail = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
   
      #Token read
        only_read = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjQ1MDYzZWZkMjI5MDVlZGVmYjcyNGQ1YWJmN2UxYSIsInN1YiI6IjY1MDM0OGQ5ZWZlYTdhMDBhYWQ4ZDE0MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CWd3TH07PtdOyidPWA3zv37iwan_lODThjB6d2whAXo"
        headers = {"accept": "application/json", "Authorization": f"Bearer {only_read}"}


         #Get the movies 
        response = requests.get(url_detail, headers=headers)
       
        #Search for movies
        if (response.status_code==200):
            movie = response.json()
            return movie
        else:
            movie = []
            print(response.status_code)
        return movie
