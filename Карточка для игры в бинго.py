'''Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) 
целые числа от 1 до 75 (включительно), при этом центральная клетка является пустой 
(она заполняется числом 0).
Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку 
для игры в бинго.'''
import random
res = [i for i in range(1,76)]
random.shuffle(res)  
bingo = [[] for i in range(5)]
for i in range(5):
    bingo[i] = res[:5]
    res = res[5:]
bingo[2][2] = 0
for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3),end='')
    print()
