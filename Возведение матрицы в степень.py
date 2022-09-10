x = int(input())
summa = 0
mat1 = [[int(i) for i in input().split()] for j in range(x)]
mat2 = [[i for i in row] for row in mat1]
mat3 = [[0]*x for i in range(x)]
y,z = int(input()),1
while z<y:
    for t in range(x):
        for i in range(x):
            for j in range(x):
                summa += mat1[j][t]*mat2[i][j]
            mat3[i][t] = summa
            summa = 0
    z+=1
    mat2,mat3 = mat3,mat2
mat3 = mat2
for i in mat2:
    print(*i)