# 1. Develop a wheel class that will contain properties corresponding to that of an individual EEPROM entry. (Raw EEPROM entry data, number of regions, whether the data can be trusted, wheel id, etc). The number of instances, or wheel objects, will be created based upon how many EEPROM entries are presented by the user. Develop methods for the wheel object as well (checksum, etc)
# 2. Develop a function parse the file and create an accurate number of wheel objects based on the EEPROM entry. 


class Wheel:
    def __init__(self):
        self.header = []
        self.regions_data = []
        self.regions = 0
        self.wheel_id = 0
        self.valid = True
    
    @staticmethod
    def get_checksum(data_section: list) -> bool:
        sum = 0
        for value in data_section:
            if isinstance(value, int) == False:
                sum += ord(value)
            else:
                sum += value
                

        return sum % 256 == 0
    

print(Wheel.get_checksum([9, 37, 0, 0, 0, 0, 0, 0, 210]))




    

