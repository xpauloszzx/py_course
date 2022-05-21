

"""Como saber se uma palavra/ string está contida em outra
sintaxe: 
x=string/palavra" in variavel
print(x) -> vai retornar true se estiver, false se nao esta
"""
#in e not in
frase="o raato roeu aa roupaa do rei de romaa"
x= "roupa" in frase
print(x) 
# Outra possibilidade:
x="roupa" not in frase

'''PS: um caractere maíusculo nao é igual a um caractere
minusculo, logo, se usar o in/in not (se tiver problemas)
com caracteres maiusculos ou minusculos tem q usar upper
ou lower
ex:
frase2= "ola meu nome é paulo"
x="Ola" in frase2 -> isso vai dar false, pois um ola esta
maiusculo e o outro minusculo
Logo:
x"="ola".upper() in frase2.upper() seria uma solução
'''
'''----------------------------------------------------
CONCATENAÇÃO: Basta ADICIONAR um + na hora de printar
ou adicionar valor a variável

str1='curso de'
str2= 'programacao em PYTHON'
str3=str1+str2
print(str3)'''


#printando coisas com string format 

dia=23
mes=12
ano=1980
cidade=input()
print(f"voce nasceu no dia {dia} de {mes} de {ano} na cidade de {cidade}")


#Caracteres de escape & tabulação
'''Sempre que eu quiser colocar um caractere especial é necessário 
utilizar o : \ , para os simbolos especiais como: ", quebra, ', etc ''' 
print('paulo sergio galdino de \n  souza') #\n faz a quebra de linha

# Quais caracteres precisa de escape?
'''\'    \"   \n   \r   \t  \b