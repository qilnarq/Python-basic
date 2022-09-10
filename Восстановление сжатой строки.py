'''Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с
 помощью кодирования повторов, и производит обратную операцию, получая исходный текст.'''

with open('Восстановление сжатой строки.txt') as a:
    c=[]
    e=[]
    d=0
    for b in a:
        i=len(b)
        for j in range(i-1):
            if b[j].isalpha():
                c.append(b[j])
            elif b[j].isdigit():
                if b[j+1].isdigit():
                    e.append(b[j]+b[j+1])
                elif b[j-1].isdigit():
                    continue
                else:
                    e.append(b[j])
    while d<len(e):
        print(c[d]*int(e[d]),end='')
        d+=1