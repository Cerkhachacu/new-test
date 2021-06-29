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
        
    def sleep(self):
        return sleep(self)

    def validate_number_input(self = "Pilih Menu : ", btz=0, btzem='Input harus besar dari 0'):
        try:
            input_user = int(input(self))
            if btz == 0:
                return input_user
            
            if input_user == 0:
                print("Warning: {}".format(btzem))

            return input_user
                
        except ValueError:
            print("Warning : Input harus dalam bentuk angka!")
            return Tools.validate_number_input(self)