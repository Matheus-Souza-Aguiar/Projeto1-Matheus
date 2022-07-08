from select import select

cont = 'sim'
while 'sim'.title():      
      
    def soma(a,b):
          return a + b 

    def multiplica(a,b):
         return a * b
    
    def divide(a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'Não é possivel dividir por zero'

    def subtrai(a,b):
         return a - b


    Seleção = {1: soma, 2: multiplica, 3: divide, 4: subtrai}   

    print('Calculadora 1.0\n')   

    print('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\n')

    select = int(input('Informe a operação? '))
    a =   float(input(f'Informe o primeiro valor que você deseja calcular: '))
    b =   float(input(f'Informe o segundo valor que você deseja calcular: '))

    resultado = Seleção[select](a,b)

    print(f'O valor do calculo é: {resultado}')
    c = resultado
        
    rept = ''
    seg = ''
    
    seg = input('Deseja continuar? sim/não: ')
    if seg == 'sim':
        while 'sim':
        
            
            print('1 - somar\n\n2 - multiplicar\n\n3 - dividir\n\n4 - subtrair\n')

            select = int(input('Informe a operação? '))
            a =   float(c)
            print(c)
            b =   float(input(f'Informe o segundo valor que você deseja calcular: '))         
        
            resultado = Seleção[select](a,b)

            print(f'O resultado é: {resultado}')
            c = resultado
        
            rept = input('Deseja continuar? sim/não: ')
            if rept == 'não':
                break
    else: 
        cont = input('Deseja fazer uma nova conta? sim/não: ')
        if cont == 'não':
            break