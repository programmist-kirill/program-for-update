from termcolor import colored
import time

import setup_module

print(colored('Start setup script','green'))

time.sleep(0.5)

print(colored('dowloaded package','white'))
#запуск скрипта загрузки пакета

print(colored('extract package','white'))
#import extract_package

print(colored('copy file','blue'))
#import copy_file

print(colored('success','green'))

print(colored('install package','white'))
#проверка существует ли файл setup.py
#import install_package
