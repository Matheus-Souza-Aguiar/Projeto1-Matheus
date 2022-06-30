from select import select

cont = 'sim'
while 'sim'.title():      
      
    def soma(a,b):
          return a + b 

    def multiplica(a,b):
         return a * b
    
    def divide(a,b):
        
        if b != 0:
           return a / b
        else:
            return 'Não é possivel dividir por 0'

    def subtrai(a,b):
         return a -  b


    Seleção = {1: soma, 2: multiplica, 3: divide, 4: subtrai}   

    print('Calculadora 1.0')   

    print('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair')

    select = int(input())
    a =   float(input(f'Informe o primeiro valor que você deseja calcular: '))
    b =   float(input(f'Informe o segundo valor que você deseja calcular: '))

    resultado = Seleção[select](a,b)

    print(f'O valor do calculo é: {resultado}')
    cont = input('Deseja continuar? sim/não:')
    if cont == 'n':
        break
