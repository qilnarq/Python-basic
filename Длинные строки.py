'''Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, 
которая выводит все строки наибольшей длины из файла, не меняя их порядок.'''

with open('lines.txt',encoding='utf-8') as f:
    b = len(max(f.readlines(),key=len).rstrip())
    f.seek(0)
    a = [i.rstrip() for i in f.readlines() if len(i.rstrip())==b]
    for i in a:
        print(i)
