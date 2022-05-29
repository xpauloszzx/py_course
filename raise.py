"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('True', 7)


# Exemplo refatorado


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')


#Ex2:
#Se os nomes nao forem femininos (terminarem com "a", gera um erro...)
def get_name(*arg):
    for i,name in enumerate(arg):
        if(type(name)is not str or name[-1] != 'a'):
            raise TypeError('Digite apenas nomes femininos')

get_name('paulinha','sandra','roberta','alexandra')
