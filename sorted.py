"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. 
O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados

Sort -> Modifica a propria lista

Sorted -> gera e retorna uma nova lista

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""

# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))




#Ex:

'''purchases = [
    {'Cliente':'Maria', 'Ultima Compra': 'PS4', 'qtd_compras': 110 },
    {'Cliente':'Paulo', 'Ultima Compra': 'Redmi note 11', 'qtd_compras': 34 },
    {'Cliente':'Sandra', 'Ultima Compra': 'Chapinha', 'qtd_compras': 750 }
]

purchases.append({'Cliente':'Natália', 'Ultima Compra': 'Iphone 13', 'qtd_compras': 230 })

purchases.append({'Cliente':'Josefa', 'Ultima Compra': 'PS4', 'qtd_compras': 635})

#Menores compradores
print(sorted(purchases,key = lambda compra : compra ['qtd_compras']))

#Maior comprador 
max_buyer= sorted(purchases, key = lambda compra : compra ['qtd_compras'],reverse=True)


max_buyer[0]['Disconto']=1-0.75
print(max_buyer[0])

#Ordenando pelo nome....

print(sorted(purchases,key = lambda username : username['Cliente']))


'''