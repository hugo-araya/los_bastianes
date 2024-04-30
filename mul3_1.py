abc = list('abcdefghijklmnopqrstuvwxyz')
lista = []
i = 0
while i < len(abc):
    lista.append(abc[i])
    i = i + 3
print(lista)
i = 0
while i < len(lista):
    abc.remove(lista[i])
    i = i + 1
print(abc)
