import os

class install_package:
    def dowloaded():
        with open('url') as file:
            url = file.read()
        
        os.system('git clone' , url)

    def extract():
        with open('extract.sh','w') as fp:
            fp.write('7z x package.zip -o"extract"')
    
    def copy_file():
        directory = 
        os.copy('extract',)