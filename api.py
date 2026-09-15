import requests

pokemon = input('Pokemon: ').strip().lower()
url= f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
resposta = requests.get(url)

print(f'\nStatus: {resposta.status_code}')

if resposta.status_code == 200:
    dados = resposta.json()
    
    nome = dados['name']
    id_pokemon = dados['id']
    altura = dados['height']
    peso = dados['name']
    
    tipos = []
    for tipo in dados['types']:
        tipos.append(tipo['type']['name'])
        
    habilidades = []
    for habilidade in dados['abilities']:
        habilidades.append(habilidade['ability']['name'])
        
    print("\n--- Pokémon ---")
    print(f"Nome: {nome}")
    print(f"ID: {id_pokemon}")
    print(f"Altura: {altura}")
    print(f"Peso: {peso}")
    print(f"Tipos: {', '.join(tipos)}")
    print(f"Habilidades: {', '.join(habilidades)}")

else:
    print('Pokemon não importado')