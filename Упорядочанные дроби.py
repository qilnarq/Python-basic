'''На вход программе подается натуральное число n. Напишите программу, которая выводит в 
порядке возрастания все несократимые дроби, заключённые между 0 и 1, знаменатель которых 
не превосходит n'''

from fractions import Fraction
from math import gcd
a = int(input())
res = set()
b,c= 1,a
for i in range(a):
    while b<c:
        res.add(Fraction(b,c))
        c-=1
    c = a
    b+=1
for i in sorted(res):
    if gcd(i.numerator,i.denominator)==1:
        print(i)
