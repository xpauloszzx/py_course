import random

  # O CAST basicamente é converter um tipo p outro
'''geralmente da problemas na hora de concatenar e printar dois tipos de variaveis diferentes'''
  #sintaxe: tipo(variavel)
'''ex:'''
num=15.9999

print(int(num)) #-> concatenação (serve para qualquer tipo de variavel)



#gerar numeros aleatorios #list / array 
"""basta importar a biblioteca random e chamar a func
abaixo:""" #random.randrange(comeco.final) -> Essa func gera numeros aleatorios dentro de determinado intervalo
num=[random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(-0,60),
    random.randrange(-0,60),
]
print(num[0:2])

#Como funciona a funcao range: 
c=5                #Basicamente o range gera números entre determinado intervalo.
 #printando valores da range
for valores in range(c):
    print(valores)
