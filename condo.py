# модуль для копирования под винду
# отдельно модули по ведроид, макось и айось(?)
# потому что везде разная хуйня, единой нет

import os
import shutil
from win32_setctime import setctime  # украл здесь https://github.com/Delgan/win32-setctime

# ЧАСТЬ ОТВЕЧАЮЩАЯ ЗА КОПИРОВАНИЕ В ВИНДЕ


def condo_win(src_file, dist_file):
    src_meta_data = os.stat(src_file)  # получаем метаданные, 7, 8, 9 - access time, modification time, creation time
    shutil.copy2(src_file, dist_file)  # глубокое копирование файла с метаданными
    setctime(dist_file, src_meta_data[9])  # меняю creation time
    os.utime(dist_file, (src_meta_data[7], src_meta_data[8]))  # меняю access time, modification time в дисте

# ЧАСТЬ ОТВЕЧАЮЩАЯ ЗА КОПИРОВАНИЕ В ВЕДРОИДЕ


def condo_android(src_file, dist_file):  # TODO Ведроид
    pass

# ЧАСТЬ ОТВЕЧАЮЩАЯ ЗА КОПИРОВАНИЕ В МАКОСИ


def condo_mac(src_file, dist_file):  # TODO Макось
    pass


def condo_os():  # TODO ПОДУМАТЬ
    print('nope')


# PROFIT
