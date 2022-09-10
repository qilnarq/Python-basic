'''На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки 
формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а 
возвращает список из чанков указанной длины.'''

string,num = [list(i) for i in input().split()],int(input())
b,j = [],0
if num > len(string):
    b.append(string[0])
    for i in range(1,len(string)):
        b[j]+=string[i]
else:
    while len(string)!=0:
        b.append(string[0])
        if len(string)==1:
            break
        for i in range(num-1):
            b[j]+=string[i+1]
        j+=1
        string = string[num:]
print(b)

