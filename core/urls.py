from django.urls import path
from core import views
urlpatterns = [
    path('', views.ListMoviesView.as_view(), name='index'),
    path('details/<int:id>/', views.DetailsMovieView.as_view(), name='details'),
]
