from django.test import TestCase

# Create your tests here.
import requests


url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&sort_by=popularity.desc"
only_read = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjQ1MDYzZWZkMjI5MDVlZGVmYjcyNGQ1YWJmN2UxYSIsInN1YiI6IjY1MDM0OGQ5ZWZlYTdhMDBhYWQ4ZDE0MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CWd3TH07PtdOyidPWA3zv37iwan_lODThjB6d2whAXo"
headers = {"accept": "application/json", "Authorization": f"Bearer {only_read}"}

response = requests.get(url, headers=headers)

data = response.json()
movies = data.get("results")

for movie in movies:
    title = movie.get("original_title", "Não tem title")
    print(title)
