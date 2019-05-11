n = int(input('Digite o valor de n: '))
soma = 0

while (n != 0):
    resto = n % 10
    n = (n - resto) // 10
    soma = soma + resto
print(soma)