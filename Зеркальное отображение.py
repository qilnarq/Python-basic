'''Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает 
её элементы относительно горизонтальной оси симметрии.'''

c = [[int(i) for i in input().split()] for j in range(int(input()))]
for i in range(len(c)//2):
    c[i],c[len(c)-1-i] = c[len(c)-1-i],c[i]
for i in c:
    print(*i)