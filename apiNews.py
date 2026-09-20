import requests
import os
from dotenv import load_dotenv

load_dotenv()

def configurar_busca():
    print("Dados necessários: ")
    local = input("Digite o local que deseja ver as noticias: ")
    idioma = input("Digite o idioma: ")
    limite= int(input("Digite o limíte de notícias: "))
    busca = input("O que deseja pesquisar? ")

    url = "https://api.thenewsapi.com/v1/news/top"

    api_token = os.getenv("THE_NEWS_API_TOKEN")

    params = {
        'api_token': api_token,
        "locale": local,
        "language": idioma,
        "limit": limite,
        "search":busca
    }
    return url, params

url, params = configurar_busca()


response = requests.get(
    url, 
    params=params,
    timeout=10
)

if response.status_code != 200:
    print(f"Erro: {response.status_code}")
    print(response.json())
    exit()

dados = response.json()
for numero, noticia in enumerate(dados["data"], start=1):
    print("=" * 60)
    print(f"NOTÍCIA {numero}")
    print("=" * 60)
    print(f"Título: {noticia['title']}")
    print(f"Fonte: {noticia['source']}")
    print(f"Publicado: {noticia['published_at']}")
    print(f"Link: {noticia['url']}")
    print()