#  1. Create a wheel class from which a seperate instance will be created for each wheel datagram in the EEPROM entry. The wheel class must have properties like id and validity that will later be displayed to the user. To create an instance, the user only needs parsed data from an EEPROM entry.
#  2. Create methods that will be used for every wheel instance, like getting the checksum. They will be called in the main.py file for all instances of WheelData. 


class WheelData:
    def __init__(self, parsed_data):

        self.header_data = parsed_data[:9]
        self.regions_data = parsed_data[9:]

        self.region_locations = {}

        self.wheel_id = 0
        self.faulty_region = []

        self.valid_data = True

    
    #  1. Create a variable to keep track of the region's sum
    #  2. Iterate through all digits in the wheel section and differentiate between letters and numbers. Add the result to the sum variable
    #  3. Return whether or not the sum yields a checksum value of 0

    # Time Complexity: O(N), where N is the length of the wheel_section list arguement. Linear time complexity
    def yield_checksum(self, wheel_section: list) -> bool:
        sum = 0
        for value in wheel_section:
            if value.isdigit():
                sum += int(value)
            else:
                sum += ord(value)

        return sum % 256 == 0
    
    #  1. Check if the checksum of the header section yields 0, proving it is a valid piece of data
    #  2. Iterate through data element in the header section and assign the locations at which every region starts and ends to the correct region
    def analyze_header(self): 
        if self.yield_checksum(self.header_data) == False:
            self.valid_data = False
        else:
            begin_idx = 9
            for idx in range(1, len(self.header_data)):
                end_idx = len(self.regions_data)
                if self.header_data[idx] != '0':
                    end_idx = self.header_data[idx]
                    self.region_locations[idx] = (begin_idx, end_idx)
                    begin_idx = self.header_data[idx]

        return self.region_locations


new_wheel = WheelData(['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '1', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '45', '4', '1', '1', '1', '3', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '200'])
print(new_wheel.analyze_header())
print(new_wheel.yield_checksum(new_wheel.header_data))
