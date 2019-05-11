n = int(input('Digite um número inteiro: '))
primo = True
divisor = 2

while divisor < n and primo:
    if n % divisor == 0:
        primo = False
    divisor = divisor + 1

if primo and n != 1:
    print('primo')
else:
    print('não primo')
