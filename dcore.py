import core
import init_linux_zip
import core_zip

class init:
    def start(action):
        core.parsing_information.start()
        
        with open('directory_to_extract') as file:
            extract_directory = file.read()
        
        with open('directory_to_archive') as file:
            directory = file.read()
        
        with open('directory_to_create_script') as file:
            directory_create = file.read()

        if action == 'load':
            init_linux_zip.start_module_init_linux()
            core_zip.write_script_linux.write(directory,extract_directory,directory_create)
            core.load_package.init_start(directory_create)