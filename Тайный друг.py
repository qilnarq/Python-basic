'''Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, 
который будет вместе с ним решать задачи по программированию.Напишите программу, которая 
случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним 
решать задачи по программированию.'''
import random
a = int(input())
b = [[input()] for i in range(a)]
c = b[:]
while len(c)!=0:
    random.shuffle(c)
    for i in range(1):
        if b[i]!=c[i]:
            print(str(*b[i]) + ' - ' + str(*c[i]))
            b = b[1:]
            c = c[1:]