"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilização do print() para debugar código é uma prática ruim.

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger





# Exemplo com o PDB - Python Debugger - Exemplo 1


# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável) ->  p_nome_variavel
# c (continua a execução - finaliza o debugging)




nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)






# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))




# Como os nomes das variávels são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel



# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.



def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""
