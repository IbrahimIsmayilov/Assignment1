#  Create an eeprom class that will have an instance created for every filename that the user provides
#  The class will have properties, like different datagrams that occur in all cartridges regardless of whether it is a wheel object inside
#  The class will have methods that create an instance of every object within the file, that identify each object, and so forth

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

    #  Time Complexity: O(N), where N equals the length of the parsed data. Linear time complexity
    def check_if_wheel(self, parsed_data: list) -> str:
        """
        Checks to see whether or not the given list of data proves an object is a wheel
        """
        for idx in range(len(parsed_data) - 4):
            if parsed_data[idx:idx+5] == ['W', 'h', 'e', 'e', 'l']:
                return True
        
    #  Time Complexity: O(N), where N equals the number of entries in the EEPROM Cartridge. Linear time complexity
    def get_objects(self, parsed_data: list) -> str:
        """
        Returns the type of object the entry belongs to in a string format
        """
        if self.check_if_wheel(parsed_data) == True:
            self.all_objects.append(wheel_class.WheelDatagram(parsed_data))
            self.wheel_objects.append(wheel_class.WheelDatagram(parsed_data))
        else:
            self.all_objects.append(entry_class.EntryDatagram)


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by checking if every wheel object has a first and second region

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def check_all_wheel_region1_2s(self):
        """
        Checks whether or not each wheel entry has a first and second region
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.check_region1_2_existence()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, analyze the header region

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def analyze_all_wheel_headers(self):
        """
        Analyzes the header region for every wheel object
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.analyze_header()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by getting all mini entry locations(beginning and ending indexes)

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def get_all_wheel_mini_entries(self):
        """
        Updates the locations(beginning and ending indexes) of every mini entry in all entries
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.get_mini_entry_locations()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by calling function from the wheel class

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def get_all_wheel_details(self):
        """
        Updates necessary details like manufacturing for every wheel
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.get_date_city_country()
            wheel_datagram.get_part_id()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by checking if every wheel object has a first and second region

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def check_all_wheel_region1_2s(self):
        """
        Checks whether or not each wheel entry has a first and second region
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.check_region1_2_existence()


    #  1. Iterate through all wheel objects
    #  2. Check if 

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def check_all_wheel_region1_2s(self):
        """
        Checks whether or not each wheel entry has a first and second region
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.check_region1_2_existence()
















    

    



    

        



