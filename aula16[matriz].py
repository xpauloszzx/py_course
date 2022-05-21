
matriz=[]                      #consiste na mesma matriz do for, mas com sintaxe diferente.
'''maior=-99999'''
l=int(input('numero de linhas: '))
c=int (input('numero de colunas: '))

for i in range(l):                   #percorrendo colunas
    linha = []                       #adicionando uma linha que trava no primeiro for
    for j in range (c):              #percorrendo valores das colunas
        elemento=input('Elemento da linha {} e coluna {}'.format(i,j))  #digitar elementos p preencher
        linha.append(int(elemento))       #armazenando valores na linha
    matriz.append(linha)                  #armazenando valores na matriz

for x in range (l):       #printando matriz
    for y in  range (c):
        print('[{}]'.format(matriz[x][y]:^3),end=' ')
    print( ) #pular uma linha
    #o ,end=' ' -> da espaço entre os elementos 
    # o :^3 serve para centralizar em 3 casas decimais (ficar mais organizado na matriz)

#verificando maior numero da matriz
'''for x in m:
    for y in n:
        if(maior<matriz[x][y]):
            maior=matriz[x][y]
print('O maior elemento é: {}'.format(maior))'''

