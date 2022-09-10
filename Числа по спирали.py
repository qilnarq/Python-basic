'''Выведите таблицу размером n×n, заполненную числами от 1 до n^2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в 
примере (здесь n=5):'''

a = int(input())
b = [[0*a for i in range(a)] for i in range(a)]
c = 1
n = len(b)
while c<=n**2:
    for j in range(-a,-1):
        if b[-a][j]==0:
            b[-a][j]=c
            c+=1
    for j in range(-a,-1):
        if b[j][a-n-1]==0:
            b[j][a-n-1]=c
            c+=1
    for j in range(a-1,-1,-1):
        if b[a-1][j]==0:
            b[a-1][j]=c
            c+=1
    for j in range(a-1,-1,-1):
        if b[j][n-(a-1)-1]==0:
            b[j][n-(a-1)-1]=c
            c+=1
    a-=1
for i in range(n):
    print(*b[i])