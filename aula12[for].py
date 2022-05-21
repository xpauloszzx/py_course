import os      #comando para limpar o prompt
os.system('cls') 
# O for vai ser utilizadao para trabalhar com coleções


'''Ex: quero imprimir elemento por elemento.''' 
'''sintaxe:                      -> Percorre toda a lista
for variavel1 in v2:        -> ps: a variável vai receber os elementos da lista
    print(variavel)         -> v2 é a variavel que será percorrida  '''   

 # Pode percorrer uma lista já declarada ou não.
carros=["HRV","GOLF","ARGO","FOCUS"]    #Percorrendo toda lista
for x in carros:
    print(x)

#programa 2: #comando de parada
for x in carros:
    if(x=='ARGO'):
        break
    print(x)

#programa 3: #pulando elemento desejado
for x in carros:
    if x=='GOLF':
        continue
    print(x)

#programa 4: [tabuada de todos os numeros]
'''for num1 in range(1,11): # a funcao range gera numeros de um intervalo a outro
    for num2 in range (1,11):
        print(f'{num1}X{num2}={num1*num2}')
    print('\n')'''



