ent = open('terr.txt')
linea = ent.readline()
while linea != '':
    linea = linea.rstrip('\n')
    lista = linea.split()
    fecha = lista[0]
    l_fecha = fecha.split('/')
    year = l_fecha[2]
    print(year)
    linea = ent.readline()
ent.close()
