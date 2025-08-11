# 1. Develop a function to read file from given file which EEPROM data and contain the data of the wheel components. 
# 2. Develop a function that checks whether or not an array of values provide a checksum of 0 or not.
# 3. Develop a function that begins to parse using by dividing the data into sections. For every wheel component, there are 3 sections. Each section ends with a checksum padding and a new one begins after up until the third section. Within each of these 3 main sections, each section has a preset amount of mini sections. The first section is called the header and consists of itself. The second section has 4 mini-sections. This includes the date, wheel id, city and country mini-components followed by a checksum phadding. The third and last section has 2 mini components called tray id and part id, which are also followed by the checksum padding. The function must return a boolean value if the cartidges have the correct data and a string otherwise that indicates where each error may be. The function must meet many requirements such as:
#           - Calculating the checksums wherever possible, at the end of each of the 3 main sections that contain a checksum padding. 
#           - Printing each possible mini-component's data of the wheel on a new line for clarity.
#           - Returning a boolean value if the cartidges have the correct data and a string otherwise that indicates where the error is located, in terms of which section or mini-entry.  

# 1
    # 1. Read the file in python 
    # 2. Store the data in a variable
    # 4. Return the variable



# Time Complexity: O(1), constant time
def read_wheel_data(filename: str) -> str:
    with open(filename, 'r') as wheel_data:
        file_contents = wheel_data.read()


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
    # 1. Loop 3 times for each of the 3 main section that contain a checksum padding
    # 2. Create a new empty list within each 3 loops to contain the list that will be evaulated for the checksum
    # 3. Within each of the 3 loops, create an iteration that iterates n amount of times, where n is the element that precedes other values before the creation of the iteration. 
    # 4. 



def parse_file(
               
    
