# возвращает свойства файла

import os.path
import time

def props(file):
    print('File         :', file)
    print('Access time  :', time.gmtime(os.path.getatime(file)))  # T последнего доступа
    print('Modified time:', time.gmtime(os.path.getmtime(file)))  # T изменения файла
    print('Change time  :', time.gmtime(os.path.getctime(file)))  # T создания (Windows), T изменения файла (Unix).
    print('Size         :', os.path.getsize(file))  # размер в байтах

