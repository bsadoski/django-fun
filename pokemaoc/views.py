from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import pokebase as pb
# Create your views here.

# Make a request to api and take some fields to our view
@login_required(login_url='/accounts/login/')
def simple(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/6')
    pokemon = response.json()
    return render(request, 'pokemaoc/simple.html', {
        'nome': pokemon['name'],
        'imgs': pokemon['sprites']
    })

def package(request):
    sprite = {}
    if 'pokemon_name' in request.GET:
        # url = 'https://api.github.com/users/%s' % username
        pokemon_name = request.GET['pokemon_name']
        sprite = {'url': pb.SpriteResource('pokemon', pokemon_name).url}
    return render(request, 'pokemaoc/package.html', {'sprite':sprite})



# https://dev.to/camerenisonfire/10-intriguing-public-rest-apis-for-your-next-project-2gbd
# https://pokeapi.co/docs/v2#pokemon
# https://github.com/PokeAPI/pokebase