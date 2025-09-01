#  1. Create a wheel class from which a seperate instance will be created for each wheel datagram in the EEPROM entry. The wheel class must have properties like id and validity that will later be displayed to the user. Instances will be created only if an entry is a wheel object
#  2. Create methods that will be used for every wheel instance, like getting the checksum. They will be called in the main.py file for all instances of WheelDatagram

import entry_class

class WheelDatagram(entry_class.EntryDatagram): 
    def __init__(self, parsed_data):
        """
        Intialize WheelDatagram class with properties that should belong to all wheel datagrams
        """
        entry_class.EntryDatagram.__init__(self, parsed_data)

        self.header_data = parsed_data[:self.all_data[0]]

        self.region_locations = {}
        self.mini_entry_locations = {}

        self.object_type = 'Wheel'
        self.wheel_id = 'No ID'

        self.date = 'No Date'
        self.city = 'No City'
        self.country = 'No Country'

        self.part_id = 'No Part ID'

        self.faulty_regions = []


    #  1. Create a variable to keep track of the region's sum
    #  2. Iterate through all digits in the wheel section and differentiate between letters and numbers. Add the result to the sum variable
    #  3. Return whether or not the sum yields a checksum value of 0

    # Time Complexity: O(N), where N is the length of the section of the wheel datagram or the list argument. Linear time complexity
    def yield_checksum(self, wheel_section: list) -> bool:
        """
        Returns whether or not an array of elements yields a checksum of 0
        """
        sum = 0
        for value in wheel_section:
            if isinstance(value, str):
                sum += ord(value)
            else:
                sum += value       

        return sum % 256 == 0
    

    #  1. Check if the checksum of the header section yields 0, proving it is a valid piece of data. If it is proven valid, continue. Else, do not check for anything else in the entry as faulty header data means the whole datagram should not be checked further. If valid, call the function that gets the beginning and ending indexes of every region in the wheel entry.
    
    #  Time Complexity: O(N), where N is the length of the header section's contents in the wheel entry. Linear Time Complexity
    def analyze_header(self): 
        """"
        Check if the header yields a checksum of 0. If it is valid data, check further and assign beginning and ending indexes of every region
        """
        if self.yield_checksum(self.header_data) == False:
            self.faulty_regions.append(('Header', "Wrong Checksum"))
        else:
            self.get_region_locations()


    #  1. Check the length of the instance's list of faulty regions
    #  2. Update the validity property of the instance accordingly

    # Time Complexity: O(1), Constant Time Complexity
    def check_validity(self) -> bool:
        """
        Updates whether or not the instance is a valid datagram based on its list of faulty regions
        """
        if len(self.faulty_regions) > 0:
            self.valid_data = False


    #  1. Iterate through data element in the header section and assign the locations at which every region starts and ends to the correct region by keeping track of the last region checked. One region's beginning signals the previous region's end 
    #  2. All regions are intially presumed to end at the end of the datagram in case no other regions are detected. Create a condition to check whether or not the iteration is at the first index to avoid any errors when checking for the last region's end. 

    #  Time Complexity: O(N), where N is the length of the header section's contents in the wheel entry. Linear Time Complexity
    def get_region_locations(self):
            """
            If it is valid data, check further and assign beginning and ending indexes of every region
            """
            for idx in range(len(self.header_data) - 1):
                if self.header_data[idx] != 0:
                    region_checked = idx + 1
                    if idx != 0:
                        self.region_locations[region_checked - 1][1] = self.header_data[idx]
                    self.region_locations[region_checked] = [self.header_data[idx], len(self.all_data)]  


    #  1. Iterate through every region in the entry
    #  2. Create beginning and ending variables that will continually change from mini entry to mini entry
    #  3. Create a variable to keep track of which mini entry will be added to the dictionary
    #  4. Iterate through the region on the condition that the mini entry's ending index is less than the region's last index. If it is, the datagram is definetely invalid and has been altered
    #  5. While iterating, continually update both the beginning and ending variables, the current mini entry's number variable, and add to the mini entries dictionary accordingly

    #  Time Complexity: O(N), where N equals the number of mini entries within the wheel datagram. Linear time complexity
    def get_mini_entry_locations(self) -> dict: 
        """
        Return all the mini entries' beginning and ending indexes in a wheel entry
        """
        for region_num in range(len(self.region_locations)):
            region_num += 1
            region = self.region_locations[region_num]
            region_data = self.all_data[region[0]:region[1]]

            mini_entry_begin = 0
            mini_entry_end = 0
            mini_entry_num = 0

            while mini_entry_end <= len(region_data) - 2:
                mini_entry_num += 1
                mini_entry_end += (region_data[mini_entry_begin]) + 1
                self.mini_entry_locations[region_num][mini_entry_num] = [region[0] + (mini_entry_begin + 1), region[0] + (mini_entry_end)]
                mini_entry_begin = mini_entry_end
            else:
                self.faulty_regions.append((region_num, "Mini entry layout is inaccurate"))
                self.check_validity()
            

    #  1. Iterate through all regions 
    #  2. If any region does not yield a checksum of 0, add it to the list property that tracks all invalid regions
    #  3. After iterating, if there were any invalid regions, change valid property of the datagram to False accordingly

    #  Time Complexity: O(N) where N equals the combined length of all the regions in the parsed data. Linear Time Complexity
    def analyze_regions(self):
        """
        Check whether or not the checksum yields 0 all regions of the datagram. Keep track of which regions have invalid data
        """
        for region_name in self.region_locations:
            region_data = self.region_locations[region_name]
            if self.yield_checksum(self.all_data[region_data[0]:region_data[1]]) != True:
                self.faulty_regions.append((region_name, "Wrong Checksum"))
        
        self.check_validity()



    #  1. Get the second mini entry's beginning and ending indexes
    #  2. Return the second mini entry's ending index

    #  Time Complexity: O(N), where N equals the number of mini entries in region 1. Constant Time Complexity
    def get_wheel_id_idx(self) -> int:
            """
            Get and return the first region and second mini entry's beginning and ending indexes
            """            
            region1_mini_entries = self.mini_entry_locations[1]
            mini_entry2_idxs = region1_mini_entries[2]
            mini_entry2_end = mini_entry2_idxs[1]
            
            return mini_entry2_end
        

    #  1. Change the Wheel ID's ASCII character to its corresponding numeric value by getting its index and altering the Wheel entry
    
    #  Time Complexity: O(1), Constant Time Complexity
    def replace_wheel_id(self, mini_entry2_end: int):
        """
        Replace the ASCII character of the wheel ID with its numeric value
        """
        wheel_id_idx = mini_entry2_end - 1
        self.all_data[wheel_id_idx] = ord(self.wheel_id)

    #  1. Get the index of the second mini entry's end and get the wheel id's index in the parsed data
    #  2. Update and replace the wheel id

    #  Time Complexity: O(1), Constant Time Complexity
    def analyze_wheel_id(self): 
        """
        Store and replace the id of the wheel component by analyzing first region 
        """
        mini_entry2_end = self.get_wheel_id_idx() - 1
        self.replace_wheel_id(mini_entry2_end)


    #  1. Iterate through all the regions and get their mini entries' locations (beginning and ending indexes)
    #  2. Display the mini entries

    #  Time Complexity: O(N), where N equals the number of mini entries within a given datagram
    def display_mini_entries(self):
        """
        Outputs all mini entries on a seperate line for clarity
        """
        for region in self.region_locations:
            for mini_entry in self.mini_entry_locations[region]:
                mini_entry_idx = self.mini_entry_locations[mini_entry]
                print(self.all_data[mini_entry_idx[0]:mini_entry_idx[1]])


    #  1. Get the first key that was inserted in the dictionary which holds all regions' beginning and ending indexes
    #  2. Get the second key that was inserted in the dictionary which holds all regions' beginning and ending indexes
    #  3. If those keys are 1 and 2, do not update anything. Else, add them to the list of faulty region and label the datagram as invalid data

    #  Time Complexity: O(1), Constant Time Complexity
    def check_region1_2_existence(self):
        """
        Checks whether or not the entry has a first and second region
        """
        first_key = next(iter(self.region_locations.keys()))
        second_key = next(iter(self.region_locations.keys()))

        if first_key != 1:
            self.faulty_regions.append((1, "First region does not exist"))
        
        if second_key != 2:
            self.faulty_regions.append((2, "Second region does not exist"))

        self.check_validity()
    

    #  1. Get the date, city and country mini entrys' locations (beginning and ending indexes)
    #  2. Update the manufacturing details of the datagram accordingly

    # Time Complexity: O(1), Constant time complexity
    def get_date_city_country(self):
        """
        Get and update the manufacturing details of the wheel datagram
        """
        date_idxs = self.mini_entry_locations[1][1]
        city_idxs = self.mini_entry_locations[1][3]
        country_idxs = self.mini_entry_locations[1][4]

        self.date = self.all_data[date_idxs[0]:date_idxs[1]]
        self.city = self.all_data[city_idxs[0]:city_idxs[1]]
        self.country = self.all_data[country_idxs[0]:country_idxs[1]]


            
    #  1. Get the location of the mini entry that contains the part id
    #  2. Update the part id detail of the datagram accordingly

    # Time Complexity: O(1), Constant time complexity
    def get_part_id(self):
        """
        Get and update the part id detail of the wheel datagram
        """
        part_id_idxs = self.mini_entry_locations[2][2]
        self.part_id = self.all_data[part_id_idxs[0]:part_id_idxs[1]]


    #  1. Return a message to the user based
            
    def __str__(self):
        if self.valid_data == True:
            message = 'Yes, a valid wheel entry datagram.'
            return message
        else:
            message = "No, here are the regions and the errors found within that proved it to be an invalid piece of data.\n"
            for faulty_region in self.faulty_regions:
                region_num = faulty_region[0]
                reason = faulty_region[1]
                message += f'Region Number: {region_num}, reason: {reason}\n'

            return message








    