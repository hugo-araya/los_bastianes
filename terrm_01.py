ent = open('terr.txt')
mayor = -1
linea = ent.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split()
    magnitud = float(lista[4])
    if magnitud > mayor:
        mayor = magnitud
    linea = ent.readline()
ent.close()
print(mayor)

