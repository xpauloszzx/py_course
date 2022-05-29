

data_base = [] 
credit_card=[]
status = False 



def registration (data_base): #DONE
    name=input("What's your name ?")
    age=int(input("What's your age ?"))
    cpf=int(input("What's your CPF ?"))
    Adress=input("What's your Adress ?")
    Login =input("What username will you want for your account ? ")
    passw=int(input("Type the password, please: "))
    balance=float(input("What's your balance? "))
    data_base.append({'name':name,'age':age,'CPF':cpf,'adress':Adress,'login':Login, 'pass':passw, 'balance':balance})


def query(data_base):
    print('Query criteria => name, CPF, adress, login: ')
    get_criteria = input().lower()
    if get_criteria == 'cpf' or get_criteria == 'pass': 
        get_querry_info = input('Type the name or CPF, login or adress...: ')
    else: get_querry_info = int(input('Type the name or CPF, login or adress...: '))
    for index, data in enumerate(data_base):
        if(data_base[index][get_criteria] == get_querry_info):
            print("The Costumer is registered!")
            print('What information you want to consult?')
            print('adress, age, balance....')
            get_info=input('Type here: ')
            print(data_base[index][get_info])

def withdraw(data_base,money_amount):

def credit_card(credit_card,data_base,bank_costumer):








'''def get():
    try: 
     get = int('Digite uma opcao: ')  #try n execpt
     if(type(get)is not int or type(get) is not float):
        raise ValueError ('Digite uma opcao valida')
    except:
        print('Type a valid type/value of data')
    return get
def menu():
    
    while()
    print('1  - Costumer registration')

    print('2  - Check the data base')

    print('3  - Withdraw Money')

    print('4  - Make your own credit card')

    print('5  - Consult all costumers')

    print('6  - Amount of cash available in the bank') # reduce 

    print('7  - The richest costumer and Poorest costumer') # MAX
    print(max(data_base,key = lambda costumer : data_base[] ))

    print('0  - Exit')
'''




 help(any)