def remove_repetidos(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return sorted(lista2)