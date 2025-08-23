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

    # Time Complexity: O(N), where N is the length of the wheel_section list arguement. Linear time complexity
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
    

    #  1. Check if the checksum of the header section yields 0, proving it is a valid piece of data. If it is proven valid, continue. Else, end the function as faulty header data means the whole datagram should not be checked further
    #  2. Iterate through data element in the header section and assign the locations at which every region starts and ends to the correct region by keeping track of the last region checked. One region's beginning signals the previous region's end. All regions are intially presumed to end at the end of the datagram in case no other regions are detected. Create a condition to check whether or not the iteration is at the first index to avoid any errors when checking for the last region's end. 
    
    #  Time Complexity: O(2N), where N is the length of the header section's contents in the checked wheel entry. Linear Time Complexity
    def analyze_header(self): 
        """"
        Check if the header yields a checksum of 0. If it is valid data, check further and assign beginning and ending indexes of every region
        """
        if self.yield_checksum(self.header_data) == False:
            self.faulty_regions.append('Header')

        else:
            last_region_checked = 0
            for idx in range(len(self.header_data) - 1):
                if self.header_data[idx] != 0:
                    if idx != 0:
                        self.region_locations[last_region_checked][1] = self.header_data[idx] + (last_region_checked + idx) + 1
                        self.region_locations[idx + 1] = [self.region_locations[last_region_checked][1], len(self.all_data)]  
                    else:
                        self.region_locations[idx + 1] = [self.header_data[idx], len(self.all_data)]  

                    last_region_checked = idx + 1
    

    #  1. Iterate through all regions 
    #  2. If any region does not yield a checksum of 0, add it to the list property that tracks all invalid regions
    #  3. After iterating, if there were any invalid regions, change valid property of the datagram to False accordingly

    #  Time Complexity: O(N) where N equals the combined length of all the regions in the parsed data. Linear Time Complexity
    def analyze_regions(self):
        """
        Check whether or not the checksum yields 0 all regions of the datagram. Keep track of which regions have invalid data
        """
        for region in self.region_locations:
            region = self.region_locations[region]
            if self.yield_checksum(self.all_data[region[0]:region[1]]) != True:
                self.faulty_regions.append(region)

        if len(self.faulty_regions) > 0:
            self.valid_data = False

    #  1. Check if the wheel entry has the first region. If so, continue. Else, the function ends there and nothing is updated.
    #  2. Store the first region's data in a new variable to avoid confusion
    #  3. Find the second mini entry and check if the elements making up the word Wheel exist. If so, update the wheel id of the instance with the number proceeding. Else, Label first region as faulty by adding to the faulty regions list and update the validity of the instance accordingly
    def get_wheel_id(self): 
        "Get and store the id of the wheel component by analyzing first region"
        if 1 in self.region_locations:
            region = self.region_locations[1]
            first_region_data = self.all_data[region[0]:region[1]]
            
            second_mini_entry_begin = first_region_data[first_region_data[0]] + 1
            second_mini_entry_end = second_mini_entry_begin + first_region_data[second_mini_entry_begin] 
            if first_region_data[second_mini_entry_begin + 1:second_mini_entry_end - 1] == ['W', 'h', 'e', 'e', 'l']:
                self.wheel_id = first_region_data[second_mini_entry_end]
            else:
                self.faulty_regions.append(1)
                self.valid_data = False
            
                        


   
    def display_mini_entries(self): ...




new_wheel = WheelData([9, 37, 0, 0, 0, 0, 0, 0, 210, 8, 2, 0, 0, 8, 13, 4, 0, 0, 6, 'W', 'h', 'e', 'e', 'l', 1, 6, 'O', 't', 't', 'a', 'w', 'a', 6, 'C', 'a', 'n', 'a', 'd', 'a', 45, 4, 1, 1, 1, 3, 9, 8, 2, 4, 8, 1, 5, 3, 5, 1, 200])
print(new_wheel.yield_checksum(new_wheel.header_data))  # True

new_wheel.analyze_header() 
print(new_wheel.region_locations)  # {1: [9, 37], 2: [37, 56]}

new_wheel.analyze_regions()
print(new_wheel.faulty_regions)  # True

new_wheel.get_wheel_id()
print(new_wheel.wheel_id)
