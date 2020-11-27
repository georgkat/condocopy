import dirparcer  # подключаю модуль-парсер
import fileprops  # подключаю модуль-свойств файла
import condo  # подключаю win-модуль для копирования
import os
# from PIL import Image  #          ЭТО ПОКА НЕ НАДО
# from PIL.ExifTags import TAGS  #  ЭТО ПОКА НЕ НАДО (РЕФЫ ПО ТЭГАМ ИЗ ПИЛА)

origin_dir = input('введи название директории для парсинга:')  # ручной ввод оригинальной директории
# origin_dir = '/Users/georgkat/Downloads/'  # заглушка к предыдущей строке
os.chdir(origin_dir)  # подключаем исходную директорию
d = os.getcwd()  # задаем путь к исходной директории как переменную

dirparcer.parce(d)  # запускаем парсер директорий

# src_file = input('Введи путь к файлу')
src_file = 'C:/testdir/1/1.jpg'
data = fileprops.props(src_file)
dist_filename = str(data[3][2]) + '-' + str(data[3][1]) + '-' + str(data[3][0]) + '_' + '1.jpg'
dist_file = 'C:/testdir/2/' + dist_filename
condo.condo_win(src_file, dist_file)
print(os.stat(src_file))
print(os.stat(dist_file))


# print(str(fileprops.props(srcfile)[3]) + '-' + str(fileprops.props(srcfile)[2]) + '-' + str(fileprops.props(srcfile)[1]))