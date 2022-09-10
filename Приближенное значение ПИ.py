'''Напишите программу, которая при помощи метода Монте-Карло определяет приближённое 
значение числа π.'''

import random
n = 10**6
k = 0
So = 2**2
 
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2+y**2<=1:
        k+=1
S = (k/n)*So
print(S/1)