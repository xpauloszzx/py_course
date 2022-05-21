#Sintaxe #if #elif #else 
''' A VANTAGEM DO ELIF É QUE O PROGRAMA NÃO TESTA MAIS A CONDICAO,
DIFERENTE DO IF''' #PS: O else só é ativado quando todas as condicoes nao funfarem

# COMPARAÇÕES; and, or 

'''a=10
b=5
op=input('Digite  o operador: ')
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print('operador invalido')'''

#Programa #2 com condicionais #media
#PS: É necessário fazer o cast para armazenar diferentes tipos (exceto:str)
n1=int (input('Digite a nota 1: '))
n2=int (input('Digite a nota 2: '))
n3=int(input('Digite a nota 3: '))
ttl= (n1+n2+n3)/3
if ttl > 3 and ttl < 7:
    print('final')
elif ttl >= 7:
    print('aprovado')
else:
    print('reprovado')


