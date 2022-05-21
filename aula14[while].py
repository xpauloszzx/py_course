# É o mesmo while do C. #programinha
import os

storage=[]    #list vazia que vai armazenar valores
i=0; media=0    
cont=input('Sup, wanna convert temperature? [S/N]').upper() 
while cont=='S':           #checagem de condicao
    fah=int(input('Type the value in fahrenheit: ')) 
    cel=((fah-32)*5)/9 
    os.system('cls')
    print(f"The temperature in Celsius is: {cel}") 
    storage.append(cel)   #armazenando os elementos digitados na list
    i+=1                #contando as vezes que os elemento foram armazenados
    cont=input('Wanna keep on converting? [S/N] ').upper()
    

print(f'The values are: {storage}') #printando todos el. da list
for x in storage:            #calculando a media
    media=(media+x)/i
print(f'The average between the temperatures are: {media} ') #printando
