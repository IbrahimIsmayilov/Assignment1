import file_parse

#  Create an eeprom class that will have an instance created for every filename that the user provides
#  The class will have properties, like different datagrams that occur in all cartridges regardless of whether it is a wheel object inside. 

class EEPROMCartridge:
    def __init__(self, filename):
        """
        Intialize properties that will be common among all cartridge files
        """
        self.filename = filename
        self.raw_data = file_parse.read_file(filename)
        self.parsed_data = file_parse.parse_file(self.raw_data)
        self.object_type = []

    