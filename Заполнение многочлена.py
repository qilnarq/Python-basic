'''На вход программе на первой строке подаются коэффициенты многочлена (целые числа), 
разделенные символом пробела и целое число x на второй строке.
Программа должна вывести одно число — значение указанного многочлена при заданном 
значении x.'''
from functools import reduce
a = [int(i) for i in input().split()]
b = [int(input())]*len(a)
def evaluate(coefficients, x):
    return reduce(lambda x,y: x+y,map(lambda x,y,z: x*y**z,a,b,[i for i in range(len(a)-1,-1,-1)]),0)
print(evaluate(a,b))
