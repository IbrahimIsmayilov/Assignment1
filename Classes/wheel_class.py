#  1. Create a wheel class from which a seperate instance will be created for each wheel datagram in the EEPROM entry. The wheel class must have properties like id and validity that will later be displayed to the user. To create an instance, the user only needs parsed data from an EEPROM entry.
#  2. Create methods that will be used for every wheel instance, like getting the checksum. They will be called in the main.py file for all instances of WheelData. 


class WheelData:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data
        self.wheel_id = 0
        self.valid = True
    
    #  1. Create a variable to keep track of the region's sum
    #  2. Iterate through all digits in the wheel section and differentiate between letters and numbers. Add the result to the sum variable
    #  3. Return whether or not the sum yields a checksum value of 0

    # Time Complexity: O(N), where N is the length of the wheel_section list arguement. Linear time complexity
    @staticmethod
    def get_checksum(wheel_section: list) -> bool:
        sum = 0
        for value in wheel_section:
            if value.isdigit():
                sum += int(value)
            else:
                sum += ord(value)

        return sum % 256 == 0

print(WheelData.get_checksum(['9', '37', '0', '0', '0', '0', '0', '0', '210']))  # True
