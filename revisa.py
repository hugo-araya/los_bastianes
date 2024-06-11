mini = 14
mayo = 14

ent = open('titanic3_nuevo.txt')
for linea in ent:
    lista = linea.rstrip('\n').split(',')
    if len(lista) < mini:
        mini = len(lista)
    if mayo > len(lista):
        mayo = len(lista)
print(mini)
print(mayo)
ent.close()
