numero = int(input('Numero: '))
lista = []
while numero != 1:
    lista.append(numero)
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
lista.append(numero)
print(lista)
print(len(lista))
