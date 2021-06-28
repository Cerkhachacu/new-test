from os import system, name
from time import sleep

class Tools:
    def clear(self='clear'):
        # for windows
        if name == 'nt':
            return  system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
           return system('clear')
        
    def check_width(self=''):
        cmd = '''
        mode con: cols=220 lines=50
        '''
        system(cmd)
        
    def sleep(self):
        return sleep(self)

    def validate_number_input(self = "Pilih Menu : "):
        try:
            return int(input(self))
        except ValueError:
            print("Warning : Input harus dalam bentuk angka!")
            return Tools.validate_number_input(self)