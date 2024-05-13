import matplotlib.pyplot as plt
import math

x = []
y1 = []
y2 = []

i = 0
while i < 10:
    x.append(i)
    y1.append(math.sin(i))
    y2.append(math.cos(i))
    i = i + 0.1

plt.plot(x, y1)
plt.plot(x, y2)
plt.title('Hola mundo')
plt.show()
