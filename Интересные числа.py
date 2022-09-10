'''На вход программе подаются два натуральных числа a и b. Напишите программу с 
использованием встроенной функции all() для обнаружения всех целых чисел в диапазоне 
[a;b], которые делятся на каждую содержащуюся в них цифру без остатка.'''

a = input()
b = input()
res = []
for i in range(int(a),int(b)+1):
    if all(list(map(lambda x: True if int(x)!=0 and int(i)%int(x)==0  else False,str(i)))):
        res.append(i)
print(*res)