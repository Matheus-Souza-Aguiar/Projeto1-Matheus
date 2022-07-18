from select import select
from selectors import SelectSelector

cont = 'sim'


def soma(paramtro1, parametro2):
    return paramtro1 + parametro2


def multiplica(parametro1, parametro2):
    return parametro1 * parametro2


def divide(parametro1, parametro2):
    try:
        return parametro1 / parametro2
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'


def subtrai(parametro1, parametro2):
<<<<<<< HEAD
    return parametro1 - parametro2


def chama_operacao(select):
    select = int(input('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\nInforme a operação? '))
    return select

SELECAO = {1: soma, 2: multiplica, 3: divide, 4: subtrai}

def valor_1():
    return float(input(f'Informe o primeiro valor que você deseja calcular: '))


def valor_2():
    return float(input(f'Informe o segundo valor que você deseja calcular: '))


def valor_3(c):
    return float(c)


def devolve_resultado(a, parametro1, parametro2):
    result = SELECAO[a](parametro1, parametro2)
    return result


def continua_conta(parametro3):
    a = chama_operacao(select)
    parametro1 = parametro3
    parametro2 = valor_2()
    parametro3 = devolve_resultado(a, parametro1, parametro2)
    print(parametro3)

    seg = input('Deseja continuar? sim/nao ' )
    if seg == 'sim':
        continua_conta(parametro3)
    elif seg == 'nao':
        centro()

def centro():
    while 'sim'.title():

        print('Calculadora 1.0\n')

        a = chama_operacao(select)
        parametro1 = valor_1()
        parametro2 = valor_2()
        parametro3 = devolve_resultado(a, parametro1, parametro2)
        print(parametro3)

        seg = input('Deseja continuar, fazer nova conta ou finalizar? continuar/nova conta/ finalizar  ')
        if seg == 'continuar':
            continua_conta(parametro3)
        elif seg == 'nova conta':
            centro()
        elif seg == 'finalizar':
            break


=======
    return parametro1- parametro2
Selececao = {1: soma, 2: multiplica, 3: divide, 4: subtrai}

def chama_operacao(select):
    select = int(input('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\nInforme a operação? '))
    return select

def valor_1():
    return float(input(f'Informe o primeiro valor que você deseja calcular: '))

def valor_2():
    return float(input(f'Informe o segundo valor que você deseja calcular: '))

def valor_3(c):
    return float(c)

def devolve_resultado(parametro1,parametro2):
    result = SelectSelector[select](parametro1, parametro2)
    return result


def continua_conta():
    chama_operacao(select)
    parametro1 = valor_3(parametro3)
    parametro2 = valor_2()
    parametro3 = devolve_resultado
    return print(devolve_resultado(parametro1, parametro3))

    seg = input('Deseja continuar o calculo? sim/nao:  ')
    if seg == 'sim':
        continua_conta()
    else:
        return ''

def centro():
        while 'sim'.title():
            
            print('Calculadora 1.0\n')
            
            chama_operacao(select)
            parametro1 = valor_1()
            parametro2 = valor_2()
            parametro3 = devolve_resultado(parametro1,parametro2)
            print(devolve_resultado(parametro1,parametro2))


            seg = input('Deseja continaur, fazer nova conta ou finalizar? continaur/nova conta/finalizar  ')
            if seg == 'continaur':
                print(continua_conta())
            elif seg == 'nova conta':
                centro()
            elif seg == 'finalizar':
                  break
                            
>>>>>>> 8e5a92bc1fb5ff4589ed71d6740e0ff400d21740
centro()