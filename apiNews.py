import requests
import os
from dotenv import load_dotenv

load_dotenv()

print("Dados necessários: ")
local = input("Digite o local que deseja ver as noticias: ")
idioma = input("Digite o idioma: ")
limite= int(input("Digite o limíte de notícias: "))

url = "https://api.thenewsapi.com/v1/news/top"

api_token = os.getenv("THE_NEWS_API_TOKEN")

params = {
    'api_token': api_token,
    "locale": local,
    "language": idioma,
    "limit": limite,
}

response = requests.get(url, params=params)

dados = response.json()
for noticia in dados['data']:
    print(noticia['title'])
    print(noticia['source'])
    print(noticia['published_at'])
    print(" ")