from django.urls import path
from core.views import ListMoviesView
urlpatterns = [
    path('', ListMoviesView.as_view(), name='index'),
]
