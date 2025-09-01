#  Create an eeprom class that will have an instance created for every filename that the user provides
#  The class will have properties, like different datagrams that occur in all cartridges regardless of whether it is a wheel object inside
#  The class will have methods that create an instance of every object within the file, that identify each object, and so forth

import entry_class
import wheel_class

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
        

    #  1. Iterate through the entire dataset 
    #  2. Check if each entry is a wheel
    #  3. If it is a wheel, add it to both the list of wheels and objects. Else, only add it to the list of entries

    #  Time Complexity: O(N), where N equals the number of entries in the EEPROM Cartridge. Linear time complexity
    def get_objects(self,) -> str:
        """
        Updates the list of entries and wheel entries by checking if each entry is a wheel object
        """
        for entry_data in self.parsed_data:
            if self.check_if_wheel(entry_data) == True:
                wheel_object = wheel_class.WheelDatagram(entry_data)
                self.all_objects.append(wheel_object)
                self.wheel_objects.append(wheel_object)
            else:
                self.all_objects.append(entry_class.EntryDatagram(entry_data))


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update their list of faulty regions with the arguement and declare their data to be not valid

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def declare_all_wheels_invalid(self, faulty_region: tuple):
        """
        Updates the list of faulty regions and the validity for all wheel entries
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.faulty_regions.append(faulty_region)
            wheel_datagram.valid_data = False


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, analyze the header region

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def analyze_all_wheels_headers(self):
        """
        Analyzes the header region for every wheel object
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.analyze_header()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by getting all mini entry locations(beginning and ending indexes)

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def get_all_wheels_mini_entries(self):
        """
        Updates the locations(beginning and ending indexes) of every mini entry in all entries
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.get_mini_entry_locations()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by calling function from the wheel class

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def get_all_wheels_details(self):
        """
        Updates necessary details like manufacturing for every wheel
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.get_date_city_country()
            wheel_datagram.get_part_id()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, analyze all regions and their checksums

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def analyze_all_wheels_regions(self):
        """
        Checks whether or not each region in the wheel entry yields a checksum value of 0
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.analyze_regions()


    #  1. Iterate through all wheel objects
    #  2. For all wheel objects, update details by checking if every wheel object has a first and second region

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def check_all_wheels_region1_2s(self):
        """
        Checks whether or not each wheel entry has a first and second region
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.check_region1_2_existence()


    #  1. Iterate through all wheel objects
    #  2. Check if all wheel objects have the same manufacturing details by comparing all 3 details from wheel to wheel

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def check_manufacturing_details(self):
        """
        Checks whether or not all wheel entries share the same manufacturing details
        """ 
        for idx in range(len(self.wheel_objects) - 1):
            if self.wheel_objects[idx].date != self.wheel_objects[idx + 1].date:
                self.declare_all_wheels_invalid((1), "Date is not the same for all wheels")
            if self.wheel_objects[idx].city != self.wheel_objects[idx + 1].city:
                self.declare_all_wheels_invalid((1), "City is not the same for all wheels")
            if self.wheel_objects[idx].country != self.wheel_objects[idx + 1].country:
                self.declare_all_wheels_invalid((1), "Country is not the same for all wheels")


    #  1. Iterate through all wheel objects
    #  2. Check if all wheel objects have the same part id by comparing it from wheel to wheel

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def check_part_ids(self):
        """
        Checks whether or not all wheel entries share the same part id
        """ 
        for idx in range(len(self.wheel_objects) - 1):
            if self.wheel_objects[idx].part_id != self.wheel_objects[idx + 1].part_id:
                self.declare_all_wheels_invalid((1, "Part ID is not the same for all wheels"))


    #  1. Iterate through all wheel objects
    #  2. Get the wheel ids of all wheel objects and have them converted to their corresponding numeric character

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def analyze_all_wheels_ID(self):
        """
        Updates and replaces the wheel id for all wheel objects
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.analyze_wheel_id()


    #  1. Iterate through all wheel objects
    #  2. Print the mini entries and the string representation of all wheels

    #  Time Complexity: O(N), where N equals the number of wheel entries in the EEPROM cartridge
    def display_all_wheels(self):
        """
        Returns the string representation of all wheel entries
        """ 
        for wheel_datagram in self.wheel_objects:
            wheel_datagram.display_mini_entries()
            print(wheel_datagram)
            print('----------------------')
            
    















    

    



    

        



