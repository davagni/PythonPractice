import math


def es_primo(numero):
    # Teorema de Wilson
    num = math.factorial(numero - 1) + 1
    if num % numero == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Ingresa un numero: '))
    if es_primo(numero) and numero != 1:
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')


if __name__ == "__main__":
    run()
