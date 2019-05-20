import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a_input = float(input('Digite o primeiro número: '))
    b_input = float(input('Digite o segundo número: '))
    c_input = float(input('Digite o terceiro número: '))
    imprime_raizes(a_input, b_input, c_input)

def  imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print('a raiz desta equação é', raiz1)
    else:
        if d < 0:
        print('esta equação não possui raízes reais')
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print('as raízes da equação são', raiz2, 'e', raiz1)


        