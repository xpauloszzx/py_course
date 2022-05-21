
#funcao que zera elementos de uma list se o numero for maior que 10

numeros=[4,10,11,25,9,8,7,5,3,50,99,40,75,23]
x=len(numeros)
def zerar (num):
    count=0
    i=0
    while i<x:
        if num[i]>10:
            num[i]=0
            count=count+1
        i+=1
    return print(num)

zerar(numeros)

