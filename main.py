# 1. Develop a function to read file from given file and return a list with seperate Wheel entries
# 1. Develop a wheel class from which there will be instances created corresponding 


# 1. 
    # 1. Create an empty list that will store seperate EEPROM entries as lists within
    # 2. Read the file and iterate through it. While all of the file characters are not read, as long as it is not an empty line, create an inner empty list and append EEPROM elements to it. Once there is an empty line, create a new list for a new EEPROM entry and continue the process
    # 3. Return the list


import string
def read_file(filename: str) -> list:
    numbers = '1234567890'
    letters = string.ascii_letters
    all_wheel_entries = []
    with open(filename) as file:
        contents = file.read()


    idx = 0
    wheel_entry = []
    while idx <= len(contents) - 1:
        if contents[idx:idx + 2] != '\n\n':
            if contents[idx] in numbers or contents[idx] in letters:
                wheel_elem = contents[idx]
                if contents[idx] in numbers:
                    while contents[idx + 1] in numbers:
                        idx += 1
                        wheel_elem += contents[idx]
                        if idx == len(contents) - 1:
                            break
                wheel_entry.append(wheel_elem)
        else:
            all_wheel_entries.append(wheel_entry)
            wheel_entry = []

        idx += 1

    all_wheel_entries.append(wheel_entry)


    return all_wheel_entries
            


            

            

        


print(read_file('colleague-file.log'))



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
            if isinstance(value, int) == False:
                sum += ord(value)
            else:
                sum += value
                

        return sum % 256 == 0
    


    

# print(Wheel.get_checksum([9, 37, 0, 0, 0, 0, 0, 0, 210]))






    

