#Funcoes e seus tipos de parâmetros

#funcoes com parametros normais:

'''def somar (n1,n2,n3): #funcoes recebendo argumentos de entrada
    r=n1+n2+n3
    print('A soma é: {}'.format(r))
    return
somar(7,8,9)
somar(12,8,1)'''

#Argumentos arbitrários (significa que pode passar uma quantidade qualquer de parametro)
#Ex1:
#A quantidade de parâmetros vão ser definidos na chamada da funcao;
 
 
'''def textos(*txt):        # <- é uma quantidade de argumentos qualquer e sem definir
    for i in txt:        #geralmente usa-se o "for" para percorrer todos os parâmetros
        print(i)

textos("ola","meu nome ","é","paulo")    #pode colocar qualquer quantidade de parametro na chamada da funcao

#EX2:
x=1
def multi(*m):
    for i in m:
       x*=i
    return print(i)

multi(8,9,7,8,5,3,2,4)'''

#EX3:  é possivel passar list como argumento também

'''valores=[1,2,3,4,5]
def soma_list(num2):
    x=0
    for i in num2:
        x+=i
    print(x)

soma_list(valores)'''

#ex4: é possivel passar matrizes como argumento tambem
'''mat=[
['Paulo','Souza','Galdino'],
['Sandra','Cristina','Santana'],
['Maria','lourdes','sant']
]
def matriz(m1):
    l=int(input('Digite o numero de linhas: '))
    c=int(input('Digite o numero de colunas: '))
    for i in range(l):
        for j in range(c):
            print('[{}] '.format(m1[i][j]))
        print()

matriz(mat)'''
