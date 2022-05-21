#AS FUNCÕES SAO  BLOCOS DE CÓDIGOS QUE SÓ SERÃO UTILIZADOS NO PROGRAMA SE FOREM CHAMADAS.
#Serve para reaproveitamento (nao ter que digitar o mesmo codigo toda hora)
#as funções só funcionam quando foram chamadas

def somar(n1,n2): #funcao somar
    r=n1+n2
    return print(r)

def sub(n1,n2): #funcao subtrair
    r=n1-n2
    return print(r)

somar(5,7)
sub(9,8)

#Funcao que chama outras funcoes:

'''def calculos(): 
    somar()
    sub()
    return

calculos()'''