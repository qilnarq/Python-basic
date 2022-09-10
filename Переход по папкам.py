'''Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в 
которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в 
лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.'''

import os
import os.path

f = open('Переход по папкам ответ.txt','w')

b = []
for cur_dir, dirs, files in os.walk('main'):
    for dir in cur_dir.split():
        for file in files:
            if '.py' in file and dir not in b:
                b.append(dir)
                f.write(dir+'\n')
f.close
    

