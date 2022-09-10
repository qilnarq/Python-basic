a = int(input())
b = [[1]*i for i in range(1,a+2)]
c = 0
for i in range(2,len(b)):
    for j in range(len(b[i-1])):
        if j!=0 and j!=len(b[i-1])-1:
            num = b[i-1][j] + b[i-1][j-1]
            b[i][j] = num
            b[i][-1-j]=num
        c+=1
    if c==2:
        num = b[i-1][j] + b[i-1][j-1]
        b[i][j] = num
        b[i][-1-j]=num
for i in range(len(b)-1):
    print(*b[i])
