'''На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу 
размером n×m заполнив её "змейкой" в соответствии с образцом.'''

a,b = map(int,input().split())
r,f = 1,0
c = [[0]*b for i in range(a)]
while r<=b*a:
    for j in range(b):
        c[f][j] = r
        r+=1
    f+=1
    if f==a:
        break
    for j in range(1,b+1):
        c[f][-j] = r
        r+=1
    f+=1
for i in range(a):
    for j in range(b):
        print(str(c[i][j]).ljust(3),end='')
    print()

        