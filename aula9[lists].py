
carros=['HRV','GOLF','ARBO','FOX']

#Imprimir da direita à esquerda (basta colocar valores negativos)
''' '''
print(carros[-1])

#Acrescentar elementos da list:
carros.append("FUSION")
carros.append("FI")
carros.append("BMW")
print(carros)


#Remover elementos da list: .REMOVE OU DEL
carros.remove(carros[0]) #pode-se digitar a "palavra" tambem
print(carros)
del carros[2]


#Descobrir o tamanho da list
"""len(variavel)"""
print(len(carros))
print("Tem",len(carros),'carros',' na lista')


# Apagar todos os elementos da lista: CLEAR
carros.clear()
print(carros)


#Copiar uma list para outra:

Carros2= list(carros)

#juntar duas listas: basta somar as duas listas
str1=['oi','ola','hello']
str2=['thanks','vlw','dank']
str3=str1+str2
print(str3)


#Como contar quantas vezes um elemento aparece na lista:
x=[1,2,3,4,5,6,7,1,8,1,9,1]
print(x.count(1))

#List em ordem alfabética ou numeral

x=["paulinho","souza","galdino","jamais"]
print(sorted(x))

