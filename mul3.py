abc = list('abcdefghijklmnopqrstuvwxyz')
i = 0
while i < len(abc):
    print(abc[i])
    abc[i] = '*'
    i = i + 3
print(abc)
cant = abc.count('*')
i = 0
while i < cant:
    abc.remove('*')
    i = i + 1
print(abc)
