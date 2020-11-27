# возвращает свойства файла

import os.path
import time

def props(file):
    return [file,
            time.gmtime(os.path.getatime(file)),
            time.gmtime(os.path.getmtime(file)),
            time.gmtime(os.path.getctime(file))]