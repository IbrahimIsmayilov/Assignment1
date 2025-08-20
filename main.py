
class Wheel:
    def __init__(self):
        self.raw_data = []
        self.regions = 0
        self.wheel_id = 0
        self.valid = True
    
    @staticmethod
    def get_checksum(data_section: list) -> bool:
        sum = 0
        for value in data_section:
            if value.isdigit():
                sum += value
            else:
                sum += ord(value)

        return sum % 256 == 0
    







    

