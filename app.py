from select import select


def soma(a,b):
     return a + b 

def multiplica(a,b):
     return a * b

def divide(a,b):
     return a / b

def subtrai(a,b):
     return a -  b

Seleção = {1: soma, 2: multiplica, 3: divide, 4: subtrai}   
print('Calculadora 1.0')   
print('1 - soma\n\n2 - multiplica\n\n3 - divide\n\n4 - subtrai')
select = int(input())
a =   float(input(f'Informe o primeiro valor que deseja somar: '))
b =   float(input(f'Informe o segundo valor que deseja somar: '))
resultado = Seleção[select](a,b)
print(f'O valor do calculo é: {resultado}')

