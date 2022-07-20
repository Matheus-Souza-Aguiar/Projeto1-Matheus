from select import select


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
    return parametro1 - parametro2


def chama_operacao(select):
    return int(input('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\nInforme a operação? '))


SELECAO = {1: soma, 2: multiplica, 3: divide, 4: subtrai}


def valor_1():
    return float(input(f'Informe o primeiro valor que você deseja calcular: '))


def valor_2():
    return float(input(f'Informe o segundo valor que você deseja calcular: '))


def devolve_resultado(operador, parametro1, parametro2):
    result = SELECAO[operador](parametro1, parametro2)
    return result


def continua_conta(parametro3):
    operador = chama_operacao(select)
    parametro1 = parametro3
    parametro2 = valor_2()
    if parametro2 == 0:
        valor0 = input('Não é possivel dividir por 0. Deseja fazer uma nova conta ou informar outro valor? Nova conta(n)/Outro valor(v): ')
        if valor0 == 'n':
            centro()
        elif valor0 == 'v':
            parametro2 = valor_2()
    parametro3 = devolve_resultado(operador, parametro1, parametro2)
    print(parametro3)

    seg = input('Deseja continuar? s/n ')
    if seg == 's':
        continua_conta(parametro3)
    elif seg == 'n':
          centro()


def centro():
    while 'sim'.title():

        print('Calculadora 1.0\n')

        operador = chama_operacao(select)
        parametro1 = valor_1()
        parametro2 = valor_2()

        if parametro2 == 0:
            valor0 = input('Não é possivel dividir por 0. Deseja fazer uma nova conta ou informar outro valor? Nova conta(n)/Outro valor(v): ')
            if valor0 == 'n':
                centro()
            elif valor0 == 'v':
                parametro2 = valor_2()

        parametro3 = devolve_resultado(operador, parametro1, parametro2)
        print(parametro3)

        seg = input('Deseja continuar, fazer nova conta ou finalizar? continuar(c)/nova conta(n)/ finalizar(f):  ')
        if seg == 'c':
            continua_conta(parametro3)
        elif seg == 'n':
            centro()
        elif seg == 'f':
            break


centro()