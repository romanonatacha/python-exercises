a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
c = int(input('Digite o terceiro número inteiro: '))

if c > b and c > a:
    if a < b:
        print('crescente')
    else:
        print('não está em ordem crescente')
else:
    print('não está em ordem crescente')
