nota = 0
suma = 0
contador = 0
cantidad = int(input('Cantidad de notas: '))
while contador < cantidad:
    nota = float(input('Nota '+str(contador + 1)+' : '))
    suma = suma + nota
    contador = contador + 1
promedio = suma / cantidad
print('Promedio: ', promedio)

                       