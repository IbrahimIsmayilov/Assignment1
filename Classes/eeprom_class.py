#  Create an eeprom class that will have an instance created for every filename that the user provides
#  The class will have properties, like different datagrams that occur in all cartridges regardless of whether it is a wheel object inside. 
#  The class will have methods that create an instance of every object within the file, that identify each object, and so forth. 

import file_parse
import entry_class
import wheel_class

class EEPROMCartridge:
    def __init__(self, filename):
        """
        Intialize properties that will be common among all cartridge files
        """
        self.filename = filename
        self.raw_data = file_parse.read_file(filename)
        self.parsed_data = file_parse.parse_file(self.raw_data)
        self.all_objects = []
        self.wheel_objects = []

    #  1. Iterate through the entire dataset 
    #  2. If the elements making up the word Wheel are encountered, return True. Else, return False. 


    def check_if_wheel(self, parsed_data: list) -> str:
        """
        Checks to see whether or not the given list of data proves an object is a wheel
        """
        for idx in range(len(parsed_data) - 5):
            if parsed_data[idx:idx+5] == ['W', 'h', 'e', 'e', 'l']:
                return True
        

    def get_objects(self, parsed_data: list) -> str:
        """
        Returns the type of object the entry belongs to in a string format
        """
        if self.check_if_wheel(parsed_data) == True:
            self.all_objects.append(wheel_class.WheelDatagram(parsed_data))
            self.wheel_objects.append(wheel_class.WheelDatagram(parsed_data))
        else:
            self.all_objects.append(entry_class.EntryDatagram)

    



    

        



