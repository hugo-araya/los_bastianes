ent = open('lee_otro.py')
linea = ent.readline().rstrip('\n')
while linea != '':
    print(linea)
    linea = ent.readline().rstrip('\n')
ent.close()