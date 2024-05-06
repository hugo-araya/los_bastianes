pal1 = 'La reina que calzaba unas zapatillas este lunes llego al Teatro Real en Madrid para asistir a un concierto organizado por la Fundacion Princesa de Girona y fue vista cojear debido a la molestia que le causa la lesion'
pal2 = 'Una mala suerte Pero esto se cura No sabia lo que tenia hasta que me hice la radiografia comento la esposa de Felipe VI a los periodistas tras ser preguntada que tal se encontraba'
pal1 = pal1.upper().split(' ')
pal2 = pal2.upper().split(' ')

# Union de ambas listas
pal3 = pal1 + pal2

pal4 = []
i = 0
while i < len(pal3):
    j = 0
    ok = True
    while j < len(pal4):
        if pal3[i] == pal4[j]:
            ok = False
        j = j + 1
    if ok == True:
        pal4.append(pal3[i])
    i = i + 1
print(pal4)
print(len(pal4))
print(len(pal1))
print(len(pal2))
print(len(pal3))

