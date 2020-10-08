# модуль-парсер каталогов на предмет структуры и jpgов

from os import listdir, chdir, path  # импорт из оси операций над катологами

# the_dir = '/Users/georgkat/Downloads/testdir'
jpg_list = list()  # список для файлов


def parce(some_dir):  # функция парсера
    chdir(some_dir)  # переходим в исходный каталог
    dir_list = listdir()  # берем список файлов в каталоге
    for filename in dir_list:  # для каждого файла решаем …
        if path.isdir(some_dir + '/' + filename):  # это каталог!?
            parce(some_dir + '/' + filename)  # если каталог - парсим его внутрь
        elif filename.lower().endswith('.jpg'):  # если не каталог, то может жпег?
            jpg_list.append(some_dir + '/' + filename)  # если жпег - добавляем его путь в список жпегов
