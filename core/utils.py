import requests
   
#Get the movies from https://developer.themoviedb.org/
def get_movies_from_api():
        
        #Popular movies
        url_popular = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
        
        #Details about movie
        url_detail = "https://api.themoviedb.org/3/movie/movie_id?language=en-US"

        #Token read
        only_read = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjQ1MDYzZWZkMjI5MDVlZGVmYjcyNGQ1YWJmN2UxYSIsInN1YiI6IjY1MDM0OGQ5ZWZlYTdhMDBhYWQ4ZDE0MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CWd3TH07PtdOyidPWA3zv37iwan_lODThjB6d2whAXo"
        headers = {"accept": "application/json", "Authorization": f"Bearer {only_read}"}
        #Get the movies 
        response = requests.get(url_popular, headers=headers)
       
        #Search for movies
        if (response.status_code==200):
            
            results = response.json()
            movies = results.get('results')
            print(movies)
        else:
            movies = []
            print(response.status_code)
        return movies




