import os
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

pal1 = 'La reina que calzaba unas zapatillas este lunes llego al Teatro Real en Madrid para asistir a un concierto organizado por la Fundacion Princesa de Girona y fue vista cojear debido a la molestia que le causa la lesion'
pal2 = 'Una mala suerte Pero esto se cura No sabia lo que tenia hasta que me hice la radiografia comento la esposa de Felipe VI a los periodistas tras ser preguntada que tal se encontraba'
pal1 = pal1.upper().split(' ')
pal2 = pal2.upper().split(' ')

# Union de ambas listas
pal3 = pal1 + pal2
pal4 = []
i = 0
while i < len(pal3):
    if pal3[i] not in pal4:
        pal4.append(pal3[i])
    i = i + 1

pal5 = []
i = 0
while i < len(pal1):
    if pal1[i] not in pal2:
        pal5.append(pal1[i])
    i = i + 1

pal5 = []
i = 0
while i < len(pal1):
    if pal1[i] not in pal2:
        pal5.append(pal1[i])
    i = i + 1

pal6 = []
i = 0
while i < len(pal2):
    if pal2[i] not in pal1:
        pal6.append(pal2[i])
    i = i + 1

pal7 = []
i = 0
while i < len(pal1):
    if pal1[i] in pal2:
        pal7.append(pal1[i])
    i = i + 1

print(pal4)
print(pal5)
print(pal6)
print(pal7)

pal8 = []
i = 0
while i < len(pal7):
    if pal7[i] not in pal8:
        pal8.append(pal7[i])
    i = i + 1
print(pal8)

