#  Create an eeprom class that will have an instance created for every filename that the user provides
#  The class will have properties, like different datagrams that occur in all cartridges regardless of whether it is a wheel object inside. 
#  The class will have methods that create an instance of every object within the file, that identify each object, and so forth. 


import file_parse

class EEPROMCartridge:
    def __init__(self, filename):
        """
        Intialize properties that will be common among all cartridge files
        """
        self.filename = filename
        self.raw_data = file_parse.read_file(filename)
        self.parsed_data = file_parse.parse_file(self.raw_data)
        self.all_objects = []


    #  1. For every object i
    def get_objects(self):
        """
        Converts all objects
        """
        
    

        



