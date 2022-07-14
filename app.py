from select import select

cont = 'sim'
while 'sim'.title():

    def soma(a, b):
        return a + b


    def multiplica(a, b):
        return a * b


    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'Não é possivel dividir por zero'


    def subtrai(a, b):
        return a - b


    Selecao = {1: soma, 2: multiplica, 3: divide, 4: subtrai}

    def chama_operacao(select):
        return int(input('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\nInforme a operação? '))


    def valor_a():
        return float(input(f'Informe o primeiro valor que você deseja calcular: '))

    def valor_b():
        return float(input(f'Informe o segundo valor que você deseja calcular: '))

    def devolve_conta(a,b):
        resultado = Selecao[select](a, b)
        return f'resultado: {resultado}'


    def continua_conta():
        chama_operacao(select)
        valor_a()
        valor_b()
        resultado = Selecao[select](a, b)
        return f'resultado: {resultado}'


    print('Calculadora 1.0\n')

    select = chama_operacao(select)
    a = valor_a()
    b = valor_b()
    print(devolve_conta(a,b))

    seg = input('Deseja continuar o calculo? sim/nao:  ')
    if seg == 'sim':
       print(continua_conta())
    else:
        cont = input('Deseja fazer uma nova conta sim/nao: ')
        if cont == 'nao':
           break
