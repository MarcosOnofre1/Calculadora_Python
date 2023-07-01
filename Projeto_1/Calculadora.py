# ** CALCULADORA WHILE **
# OBERVAÇÃO: .lower() = significa que tudo (str) vai ser em minusculo
# OBV: .startswith('letra') = significa que a letra que estiver dentro do (),
#                             é de onde vai começar o comando.


while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except numeros_validos.DoesNotExist:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas operadores.')
        continue

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)

    sair = input('Voce deseja [s]air?: ').lower().startswith('s')

    if sair is True:
        break
