#É semelhante a uma list, porém no dicionario nós podemos escolher a localização não só como um número, como as listas.
'''Geralmente nas listas temos o endereço como: variavel[0],variavel[1],etc. 
No dicionary, ao invés das posições serem números, são qualquer tipo de nome. Ex: variavel[nome],variavel[idade].
É composto pelas chaves e valores. As chaves são os endereços, os valores são o conteúdo.'''

#Exemplo de Lista

pessoas={    
    'nome':'Gustavo',
    'sexo':'M',
    'idade':22
}
#Formas de printar uma lista
'''print(pessoas['sexo'])  #printando elemento 
del pessoas['sexo']        #deletando o elemento da posição
print(pessoas.keys())      #printando apenas a localização "keys"
print(pessoas.values())    #printando apenas os valores dentro da localização "values"
print(pessoas.items())     #printando todos os itens(keys and values)
for k,v in pessoas.items():     #printando todos os itens(keys and values)   
    print('{} = {}'.format(k,v))'''

#Adicionando um elemento: #nao necessita utilizar o append

'''pessoas['peso']=98.5'''

#Criando um dicionário dentro de uma lista:      #cada elemento da list vai ser um dicionário
'''brasil=[]

estado1={
    'uf':'Rio de Janeiro',
    'sigla':'RJ'
}
estado2={
    'uf':'Sao Paulo',
    'sigla':'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)                #ou brasil[0]
print(brasil[0]['uf'])'''

#Programa de exemplo:

estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=input('Unidade Federativa: ')
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

print(brasil[0]['uf'])
print( )
print(brasil)

#printando bonitinho:
for l in brasil:             #1º for : lista
    for d in l.values():     #2º for : dictionary
        print(d,end= ' ')
    print()
