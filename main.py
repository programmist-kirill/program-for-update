import os

import dcore

class init:
    def start():
        directory_to_program = input('Где находится программа: ')
        name_user = input('Введите имя пользователя: ')

        with open('directory_program','w') as fp:
            fp.write(directory_to_program)
        
        with open('name_user','w') as fp:
            fp.write(name_user)

        

init.start()

if os.path.exists('action'):
    with open('action') as file:
        action = file.read().strip()
    

else:
    
    a = True
    while a == True:
        print('ожидание вызова')
        if os.path.exists('action'):
            with open('action') as file:
                action = file.read().strip()
                a = False
                break
        else:
            a = True
            continue


dcore.init.start(action)