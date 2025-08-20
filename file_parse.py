# 1. Develop a function to read file from given file and return a list with seperate Wheel entries


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

        
            
            
        
               
    

        
    
        
