'''На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает 
матрицу размером n×m заполнив её "диагоналями" в соответствии с образцом.'''

a,b = map(int,input().split())
c = [[0]*b for i in range(a)]
r = 1
for j in range(a+b-1):
    for i in range(a):
        if j-i in range(b):
            c[i][j-i] = r
            r+=1
for i in c:
    print(*i)