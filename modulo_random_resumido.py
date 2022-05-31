
#Lib random... 

import random 
lista1=['a','b','c','d','e']
random.shuffle(lista1) #=> Embaralha uma lista 
print(lista1)
print(random.choice(lista1)) #=> Faz uma escolha aleatoria de um elemento da lista
print(random.randint(0,100)) #=> Gera um numero inteiro pseudo aleatorio no intervalo (inicio,fim)
print(random.uniform(0,500)) #=> Gera um numeor real pseudo aleatorio no intervalo (inicio,fim)
print(random.sample(lista1,3)) #=> Obter uma amostra aleatoria de tamanho n do iterável

#Ex's:
print(list(random.randint(dado,100) for dado in range(10)))
#Ex2
mega_sena= [dado for dado in range(61)] #Gerando cartela de 60 nums
choice = random.sample(mega_sena,5) #Escolhendo 5 dos itens da cartela aleatoriam.
print(choice)

print(dir([]))




