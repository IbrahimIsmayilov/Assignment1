#  1. Create a wheel class from which a seperate instance will be created for each wheel datagram in the EEPROM entry. The wheel class must have properties like id and validity that will later be displayed to the user. To create an instance, the user only needs parsed data from an EEPROM entry
#  2. Create methods that will be used for every wheel instance, like getting the checksum. They will be called in the main.py file for all instances of WheelData

class WheelData:
    def __init__(self, parsed_data: list):
        """
        Intialize WheelData class with properties that should belong to all wheel datagrams
        """
        self.all_data = parsed_data
        self.header_data = parsed_data[:self.all_data[0]]

        self.region_locations = {}

        self.wheel_id = 'No ID'

        self.faulty_regions = []

        self.valid_data = True


    #  1. Create a variable to keep track of the region's sum
    #  2. Iterate through all digits in the wheel section and differentiate between letters and numbers. Add the result to the sum variable
    #  3. Return whether or not the sum yields a checksum value of 0

    # Time Complexity: O(N), where N is the length of the wheel_section list argument. Linear time complexity
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
    

    #  1. Check if the checksum of the header section yields 0, proving it is a valid piece of data. If it is proven valid, continue. Else, end the function as faulty header data means the whole datagram should not be checked further. Else, call the function that gets the beginning and ending indexes of every region in the wheel entry.
    
    #  Time Complexity: O(N), where N is the length of the header section's contents in the wheel entry. Linear Time Complexity
    def analyze_header(self): 
        """"
        Check if the header yields a checksum of 0. If it is valid data, check further and assign beginning and ending indexes of every region
        """
        if self.yield_checksum(self.header_data) == False:
            self.faulty_regions.append('Header')
        else:
            self.get_region_locations()


    #  1. Iterate through data element in the header section and assign the locations at which every region starts and ends to the correct region by keeping track of the last region checked. One region's beginning signals the previous region's end. 
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


    #  1. Create an empty dictionary that hold the beginning and ending indexes of every mini entry in a region. Also create a list that will hold the data that corresponds to the region number given
    #  2. Create beginning and ending variables that will continually change from mini entry to mini entry
    #  3. Create a variable to keep track of which mini entry will be added to the dictionary. 
    #  4. Iterate through the region on the condition that the mini entry's ending index is less than the region's last index. If it is, the datagram is definetely invalid and has been altered
    #  5. While iterating, continually update both the beginning and ending variables, the current mini entry's number variable, and add to the dictionary accordingly
    #  6. Return the dictionary

    #  Time Complexity: O(N), where N equals the number of mini entries within a region. Linear time complexity
    def get_mini_entry_locations(self, region_num: int) -> dict: 
        """
        Return all the mini entries' beginning and ending indexes in a dictionary
        """
        region = self.region_locations[region_num]
        region_data = self.all_data[region[0]:region[1]]
        mini_entry_locations = {}
        mini_entry_begin = 0
        mini_entry_end = 0
        mini_entry_num = 0

        while mini_entry_end <= len(region_data) - 2:
            mini_entry_num += 1
            mini_entry_end += (region_data[mini_entry_begin]) + 1
            mini_entry_locations[mini_entry_num] = [region[0] + (mini_entry_begin + 1), region[0] + (mini_entry_end)]
            mini_entry_begin = mini_entry_end
            

        return mini_entry_locations

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
                self.faulty_regions.append(region_name)
        
        if len(self.faulty_regions) > 0:
            self.valid_data = False


    #  1. Get first region's beginning and ending indexes
    #  2. Get the second mini entry's beginning and ending indexes
    #  3. Return the first region's and the second mini entry's beginning and ending indexes

    #  Time Complexity: O(N), where N equals the number of mini entries in region 1. Constant Time Complexity
    def get_wheel_id_idx(self):
            """
            Get and return the first region and second mini entry's beginning and ending indexes
            """
            region1_idxs = self.region_locations[1]
            region1_data = self.all_data[region1_idxs[0]:region1_idxs[1]]
            

            region1_mini_entries = self.get_mini_entry_locations(1)
            mini_entry2_idxs = region1_mini_entries[2]
            mini_entry2_begin = mini_entry2_idxs[0]
            mini_entry2_end = mini_entry2_idxs[1]
            
            

            return region1_data, mini_entry2_begin, mini_entry2_end
    

    #  1. Get the first key that was inserted in the dictionary which holds all regions' beginning and ending indexes
    #  2. If that key is 1, return True as it proves that the entry does have a first region

    #  Time Complexity: O(1), Constant Time Complexity
    def check_region1_existence(self):
        """
        Checks whether or not the entry has a first region
        """
        first_key = next(iter(self.region_locations.keys()))

        if first_key == 1:
            return True
        

    #  1. Change the Wheel ID's ASCII character to its corresponding numeric value by getting its index and altering the Wheel entry
    
    #  Time Complexity: O(1), Constant Time Complexity
    def replace_wheel_id(self, mini_entry2_end: int):
        """
        Replace the ASCII character of the wheel ID with its numeric value
        """
        wheel_id_idx = self.region_locations[1][0] + mini_entry2_end
        self.all_data[wheel_id_idx] = ord(self.wheel_id)

    #  1. Check if the datagram contains the letters of Wheel in order and if so, update the wheel ID to match the value after
    #  2. Return true to confirm the Wheel id's existence
    def get_wheel_id(self, region1_data, mini_entry2_begin, mini_entry2_end):
        """
        Checks the wheel id's existence and update the Wheel ID accordingly
        """
        if region1_data[mini_entry2_begin + 1:mini_entry2_end] == ['W', 'h', 'e', 'e', 'l']:
            self.wheel_id = str(region1_data[mini_entry2_end])
            return True


    #  1. Check if the wheel entry has the first region by calling a helper function that returns True if so
    #  2. Get the indexes of the second mini entry and check for the wheel id's existence. If so, update and replace the wheel existence. Else, label the whole datagram and the first region as faulty, invalid data


    #  Time Complexity: O(1), Constant Time Complexity
    def analyze_wheel_id(self): 
        """
        Get and store the id of the wheel component by analyzing first region 
        """
        if self.check_region1_existence() == True:
            region1_data, mini_entry2_begin, mini_entry2_end = self.get_wheel_id_idx()
            wheel_exists = self.get_wheel_id(region1_data, mini_entry2_begin, mini_entry2_end)
            if wheel_exists == True:
                self.replace_wheel_id(mini_entry2_end)
            else:
                self.faulty_regions.append(1)
                self.valid_data = False
            
            




new_wheel = WheelData([9, 40, 0, 0, 0, 0, 0, 0, 207, 8, 2, 0, 0, 8, 13, 4, 0, 0, 6, 'W', 'h', 'e', 'e', 'l', 1, 6, 'O', 't', 't', 'a', 'w', 'a', 6, 'C', 'a', 'n', 'a', 'd', 'a', 45, 4, 1, 1, 1, 3, 9, 8, 2, 4, 8, 1, 5, 3, 5, 1, 200])
print(new_wheel.yield_checksum(new_wheel.header_data))  # True

new_wheel.analyze_header() 
print(new_wheel.region_locations)  # {1: [9, 40], 2: [40, 56]}

new_wheel.analyze_regions()
print(new_wheel.faulty_regions)  # []

new_wheel.analyze_wheel_id() 
print(new_wheel.wheel_id)  # 1
print(new_wheel.all_data)  # [9, 40, 0, 0, 0, 0, 0, 0, 207, 8, 2, 0, 0, 8, 13, 4, 0, 0, 6, 'W', 'h', 'e', 'e', 'l', 49, 6, 'O', 't', 't', 'a', 'w', 'a', 6, 'C', 'a', 'n', 'a', 'd', 'a', 45, 4, 1, 1, 1, 3, 9, 8, 2, 4, 8, 1, 5, 3, 5, 1, 200]
new_wheel.analyze_regions()
print(new_wheel.faulty_regions)  # [1]

print(new_wheel.get_mini_entry_locations(1))  # {1: [10, 18], 2: [19, 25], 3: [26, 32], 4: [33, 39]} 






    