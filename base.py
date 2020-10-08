import dirparcer  # подключаю модуль-парсер
import fileprops  # подключаю модуль-свойств файла
import os
# from PIL import Image
# from PIL.ExifTags import TAGS, GPSTAGS

os.chdir(r'/Users/georgkat/Downloads/')  # подключаем исходную директорию
d = os.getcwd()  # задаем путь к исходной директории как переменную

dirparcer.parce(d)  # запускаем парсер директорий
# for jpg in dirparcer.jpg_list:  # для каждой строки в списке жпегов
#     fileprops.props(jpg)  # печатаем этот жпег
#     print('__')



# jpglist = list()
# dirlist = os.listdir()
#
# for i in enumerate(dirlist):
#     if i[1].lower().endswith('.jpg'):
#         file = os.getcwd() + '/' + i[1]
#         src = Image.open(file)
#         data_exif = src._getexif()
#         jpglist.append([file, data_exif])
#
# for jpg in jpglist:
#     print(jpg[0], 'EXIF:', jpg[1])

# src1 = Image.open("/Users/georgkat/Downloads/20200719_034422-DSC01261.JPG")
# src2 = Image.open("/Users/georgkat/Downloads/20200904_151234cr.JPG")
# data_exif = src2._getexif()

# for row in sorted(data_exif):
#     print(row, ':', data_exif[row])


# print(data_exif[34853])
# print(GPSTAGS)
#
# for i in data_exif[34853]:
#     print(GPSTAGS[i], ':', data_exif[34853][i])
