#Calculadora while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador(+ - / *): ')

    resultado = (numero_1 + operador + numero_2)
    print(resultado)


    sair = input('Quer sair? [s]im: ').lower().startswith()

    if sair is True:
        break