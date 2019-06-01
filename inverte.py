lista = []
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    lista.append(n)

for i in reversed(lista):
    if i != 0:
        print(i)