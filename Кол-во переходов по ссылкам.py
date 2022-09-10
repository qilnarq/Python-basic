'''Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, 
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за 
один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML 
документы.'''
from bs4 import BeautifulSoup
import requests

a,b = input(),input()
count = 1
res = requests.get(a)
f = BeautifulSoup(res.text,"lxml")
c = f.findAll('a') # список из url ссылок с тегами 'a' на странице (а)
for i in c:
    res = requests.get(i.get('href'))
    f = BeautifulSoup(res.text,"lxml")
    c = f.findAll('a')# список из url ссылок с тегами 'a' на странице (с)
    for j in c:
        if b==j.get('href'):
            print("Yes")
            count = 0
            break
    if count==0:
        break
    count = 2
if count==2:
    print("No")
    