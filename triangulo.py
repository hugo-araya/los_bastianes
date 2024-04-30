altura = int(input('Altura del triangulo: '))
i = 0
while i < altura:
    j = 0
    sal = ''
    while j < i +1:
        sal = sal + '*'
        j = j + 1
    print (sal)
    i = i + 1
