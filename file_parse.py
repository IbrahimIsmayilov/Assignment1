# 1. Develop a function to read file from given file which EEPROM data and contain the data of the wheel components. 
# 2. Develop a function that checks whether or not an array of values provide a checksum of 0 or not.
# 3. Develop a function that begins to parse using by dividing the data into sections. For every wheel component, there are 3 sections. Each section ends with a checksum padding and a new one begins after up until the third section. Within each of these 3 main sections, each section has a preset amount of mini sections. The first section is called the header and consists of itself. The second section has 4 mini-sections. This includes the date, wheel id, city and country mini-components followed by a checksum phadding. The third and last section has 2 mini components called tray id and part id, which are also followed by the checksum padding. The function must return a boolean value if the cartidges have the correct data and a string otherwise that indicates where each error may be. The function must meet many requirements such as:
#           - Calculating the checksums wherever possible, at the end of each of the 3 main sections that contain a checksum padding. 
#           - Printing each possible mini-component's data of the wheel on a new line for clarity.
#           - Returning a boolean value if the cartidges have the correct data and a string otherwise that indicates where the error is located, in terms of which section or mini-entry.  

# 1
    # 1. Create a list variable to store the seperate wheel data components
    # 2. Read the file in python 
    # 3. Seperate the wheel componenets into 4 seperate strings with 4 different wheel componenets
    # 4. Within these 4 strings, replace them with lists instead where within each list, all pieces of data within each wheel componenent is a seperate element. 
    # 5. Return the list



# Time Complexity: O(1), constant time
import re
def read_wheel_data(filename: str) -> str:
    with open(filename, 'r') as wheel_data:
        file_contents = re.split(r'\n\s*\n', wheel_data.read())
        for idx in range(len(file_contents)):
            new_wheel_data = ''
            for character_idx in range(len(file_contents[idx])):
                if file_contents[idx][character_idx] != ' ' and file_contents[idx][character_idx] != '\n':
                    print(file_contents[idx][character_idx])
                    new_wheel_data += file_contents[idx][character_idx]
            file_contents[idx] = new_wheel_data



    return file_contents

print(read_wheel_data('colleague-file.log'))
    
# 2
    # 1. Create a sum variable
    # 2. Iterate through the list and check if it is a digit. If so, add the raw value to the sum variable. Otherwise, add the number associated with the unicode character to the sum variable
    # 3. Return whether or not the checksum evaluates to 0 with a Bool value

# Time Complexity: O(N), where N is the length of the given list. Linear time complexity
def get_checksum(lst: list) -> bool:
    sum = 0
    for value in lst:
        if value.isdigit():
            sum += value
        else:
            sum += ord(value)

    return sum % 256 == 0

# 3
    # 1. Create a section variable that keeps track of which section I am in. 
    # 2. Loop 3 times for each of the 3 main section that contain a checksum padding
    # 3. Create a new empty list within each 3 loops to contain the list that will be evaulated for the checksum
    # 4. Within each of the 3 loops, create an iteration that iterates n amount of times, where n is the element that precedes other values before the creation of the iteration. 
    # 5. At the end of each main iteration, run the get_checksum() function with the list as arguement. If it returns false, break the loop, else continue.
    # 6. Return a tuple in the format of (whether or not the program finished (bool value), section last checked value (int)) if checksum returns false


def parse_file(file_contents: str) -> tuple:
    section_num = 0
    while section_num < 4:
        section_num += 1
        
               
    
