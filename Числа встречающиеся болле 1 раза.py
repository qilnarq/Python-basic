'''Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в 
одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.'''

a=sorted([int(i) for i in input().split()])
b=[]
c=1
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c+=1
    elif c>1:
        b.append(a[i])
        c=1
if c>1:
    b.append(a[i])
for i in b:
    print(i,end=' ')
# первая версия

a=sorted([int(i) for i in input().split()])
b=[]
for i in a:
    if a.count(i)>1 and i not in b:
        b.append(i)
        print(i,end=' ')
# Вторая версия