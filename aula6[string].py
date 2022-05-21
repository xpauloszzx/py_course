#STRINGS PYTHON

"""Em string pode-se imprimir de uma posição a outra 
com a sintaxe abaixo:
print(variavel[inicio:limite)])"""
curso="Paulinho Souza"
print(curso[0:50])
"""--------------------------------------------------"
Tamanho de uma string: 
É dado pela func:
len(variavel)"""
print("SIZE: "+str(len(curso)))
"""-----------------------------------------------
remover espacos do inicio e fim da string: 
variavel.strip()
"""
print(curso.strip()) #retirando espacos
print("size strip=",str(len(curso.strip())))
#^ mostrando tam da string sem espacos
"""----------------------------------------------
converter string para minusculo
variavel.lower()"""
print(curso.lower())
"""---------------------------------------------
Converter string para maiúsculo 
variavel.upper()"""
print(curso.upper())
""" obs pode ser usada duas funcoes tambem, exemplo:
"""
print(curso.upper().strip())
'''----------------------------------------------
Substituicao de strings:
sintaxe:
variavel.replace("original",substituido")'''
curso.replace(curso,"hello")
print(curso.replace(curso,"hello"))
'''------------------------------------------------
Dividir string
basicamente a func "split" vai ser usada para remover 
certo "caractere" da string e corta-la em pedaços.
sintaxe:
variavel.split("caractere")'''
a=curso.split(" ")
print(a[0:2])






"""-------------------------------------------------
RESUMO DA AULA: X é a variável

x="Paulinho souza"
print(x[5:10]) -> imprime a string de uma pos. a outra
print(curso.strip()) -> remove o espaço no começo e final da string
print(x.lower()) -> transforma toda string em minusculo
print(x.upper()) -> transforma toda string em maiusculo
print(curso.replace("origem","substituto")) 
-> Substitui strings, serve nao apenas para string,
mas para palavras tambem.
x.split("caractere") -> separa a string em varios pedacos
assim que localizar o caractere dentro de aspas
print(len(x)) -> imprime o tamanho da string

