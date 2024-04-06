from django.urls import path
from .views import search_animals

urlpatterns = [
    path('search/', search_animals, name='search_animals'),
    
]

# URl da pesquisa