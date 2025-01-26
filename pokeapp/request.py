import os
import sys
import django
from django.contrib.auth.models import User

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'pokemonologia.settings'

django.setup()

from pokeapp.models import Card
import requests
from django.core.files import File
from io import BytesIO

admin_user = User.objects.filter(username="admin").first()

if not admin_user:
    raise ValueError("Usuário 'admin' não encontrado. Crie o usuário antes de executar o script.")

pokemons = [
    ("Rillaboom", "Grass", 100, 120, 90),
    ("Incineroar", "Fire", 95, 115, 90),
    ("Kyogre", "Water", 100, 150, 90),
    ("Miraidon", "Electric", 100, 120, 90),
    ("Volcarona", "Bug", 85, 135, 105),
    ("Tornadus", "Flying", 100, 125, 90),
    ("Terapagos", "Normal", 100, 85, 75),
    ("Urshifu", "Fighting", 100, 130, 90),
    ("Salazzle", "Poison", 68, 64, 60),
    ("Calyrex", "Ghost", 100, 130, 85),
    ("Chi-Yu", "Dark", 100, 120, 85),
    ("Farigiraf", "Psychic", 90, 100, 70),
    ("Zamazenta", "Steel", 100, 135, 115),
    ("Ogerpon", "Rock", 100, 120, 90),
    ("Ursaluna", "Ground", 130, 140, 90),
    ("Calyrex", "Ice", 100, 130, 85),
    ("Raging Bolt", "Dragon", 100, 150, 85),
    ("Flutter Mane", "Fairy", 55, 135, 90),
]

def baixar_imagem(nome_pokemon):
    url = f"https://img.pokemondb.net/artwork/avif/{nome_pokemon.lower()}.avif"
    resposta = requests.get(url)
    imagem = BytesIO(resposta.content)
    return File(imagem, name=f"{nome_pokemon.lower()}.avif")

for nome, classe, hp, ataque, defesa in pokemons:
    imagem = baixar_imagem(nome)
    card = Card(
        nome=nome,
        classe=classe.capitalize(), 
        defesa=defesa,
        ataque=ataque,
        hp=hp,
        descricao=f"O Pokémon {nome} é o mais forte da classe {classe}.",
        foto=imagem,
        user=admin_user
    )
    card.save()

print("Pokémons adicionados com sucesso!")
