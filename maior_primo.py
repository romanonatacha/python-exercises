def éprimo(k):
    fator = 2
    while (k % fator != 0) and (fator <= k / 2):
        fator = fator + 1
    if k % fator == 0:
        return False
    else:
        return True

primo = 2
n = int(input('Digite um número: '))
i = 2
while i <= n:
    if éprimo(i):
       primo = i
    i = i + 1
    
print(primo)