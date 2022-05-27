"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

#filter sintax:
#filter(function,iterable)

#A funcao deve retornar alguma operacao de condicao (true ou falso) p fazer a filtração...

OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.










Ex1:

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a funcão map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.



res = filter(lambda valor: valor > media, dados)
print(list(res))







Ex2:


Remoção de dados faltantes: 

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))






# A diferenca entre map() e filter() é:


# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.








# Ex.3: Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
"""





#Ex.4:

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutrura é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)


#EX 5:

#Filtrando estudante q obteve maior nota...

students=[{'Nome':'Paulo','Nota':7.5} ,{'Nome':'Gabriel','Nota': 4.7},{'Nome':'Joana', 'Nota':5.5}, {'Nome':'Iara', 'Nota': 9.3}]

print(list(filter(lambda Alunos : Alunos['Nota']>7,students)))
