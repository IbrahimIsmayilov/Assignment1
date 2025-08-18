# # 1. Develop a function to read file from given file which EEPROM data and contain the data of the wheel components. 
# # 2. Develop a function that checks whether or not an array of values provide a checksum of 0 or not.
# # 3. Develop a function that begins to parse using by dividing the data into sections. For every wheel component, there are 3 sections. Each section ends with a checksum padding and a new one begins after up until the third section. Within each of these 3 main sections, each section has a preset amount of mini sections. The first section is called the header and consists of itself. The second section has 4 mini-sections. This includes the date, wheel id, city and country mini-components followed by a checksum phadding. The third and last section has 2 mini components called tray id and part id, which are also followed by the checksum padding. The function must return a boolean value if the cartidges have the correct data and a string otherwise that indicates where each error may be. The function must meet many requirements such as:
# #           - Calculating the checksums wherever possible, at the end of each of the 3 main sections that contain a checksum padding. 
# #           - Printing each possible mini-component's data of the wheel on a new line for clarity.
# #           - Returning a boolean value if the cartidges have the correct data and a string otherwise that indicates where the error is located, in terms of which section or mini-entry.  


# # 1

#     # 1. Open and read the file
#     # 2. Split different wheel datagrams into different elements and store them in a list. This can be achieved through importing the RegEx module and using the built in split function. 
#     # 3. Iterate through each element and update with an element that does not contain irrelevant whitespace or newline characters
#     # 4. Return the list



# # Time Complexity: O(2N), where N = the length of the given file. Linear time complexity. The main contributors are the .read() function and iterating through all of the characters in the file to remove whitespace and newline characters. 
# import re
# def read_file_data(filename: str) -> str:

    

# print(read_wheel_data('colleague-file.log'))
    
# # 2
#     # 1. Create a sum variable
#     # 2. Iterate through the list and check if it is a digit. If so, add the raw value to the sum variable. Otherwise, add the number associated with the unicode character to the sum variable
#     # 3. Return whether or not the checksum evaluates to 0 with a Bool value

# # Time Complexity: O(N), where N is the length of the given list. Linear time complexity
# def get_checksum(lst: list) -> bool:
#     sum = 0
#     for value in lst:
#         if value.isdigit():
#             sum += value
#         else:
#             sum += ord(value)

#     return sum % 256 == 0

# # 3
#     # 1. Create a section variable that keeps track of which of the 3 sections of the wheel component the function is iterating through
#     # 2. Loop 3 times for each of the 3 main section that contain a checksum padding
    
#     # 3. Within each of the 3 loops, create an iteration that iterates n amount of times, where n is the element that precedes other values before the creation of the iteration. 
#     # 5. At the end of each main iteration, run the get_checksum() function with the list as arguement. If it returns false, break the loop, else continue.
#     # 6. Return a tuple in the format of (whether or not the program finished (bool value), section last checked value (int)) if checksum returns false


# def parse_file(file_contents: str) -> tuple:
#     for wheel_data in file_contents:
#         for outer_section_num  in range(1, 4):
#             pass

        
            
            
        
               
    

        
    
        
