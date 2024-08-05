import os
import time


class load_package:
    def init_start(directory_create):
        os.system('sudo sh ' + directory_create + '/script.sh')
        
    def start(directory_to_script):
        print('запуск скрипт установки')
        os.system('python ' + directory_to_script + '/setup.py')

class parsing_information:
    def start():
        with open('information', 'r') as file:
        # Читаем все строки из файла
            lines = file.readlines()

        # Проверяем, что в файле достаточно строк
        if len(lines) >= 7:
            # Записываем каждую строку в соответствующий файл
            with open('name_package', 'w') as name_file:
                name_file.write(lines[0].strip())  # Имя пакета

            with open('version', 'w') as version_file:
                version_file.write(lines[1].strip())  # Версия

            with open('directory_to_script', 'w') as directory_to_script:
                directory_to_script.write(lines[2].strip())  # Директория скрипта

            with open('directory_to_extract','w') as directory_to_extract:
                directory_to_extract.write(lines[3].strip())  # Директория для распаковки

            with open('directory_to_archive','w') as directory_to_archive:
                directory_to_archive.write(lines[4].strip())  # Директория до архива

            with open('directory_to_create_script','w') as directory_to_create_script:
                directory_to_create_script.write(lines[5].strip())  # Директория для создания скрипта

            with open('url','w') as url:
                url.write(lines[6].strip())  # URL (откуда скачивать пакет)
        else:
            print("Файл information должен содержать как минимум 7 строки.")


