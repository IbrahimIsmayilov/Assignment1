# 1. Develop a function to read file from given file and return the contents
# 2. Develop a function to parse the contents of the file and place them in seperate elements


# 1. 
    #  1. Reads the file and returns the contents stored in a variable
    #  2. Returns the contents stored in a variable in string format 


# Time Complexity: O(N), where N is the amount of characters in the file or the length of the file contents. Linear time complexity
def read_file(filename: str) -> list[str]:
    """"
    Reads the contents of the file and stores it in a variable in string format. Returns the variable to the user
    """

    with open(filename) as file:
        raw_wheel_data = file.read()

    return raw_wheel_data

file_contents = read_file('colleague-file.log')


# 2. 
    # 1. Create a new list that contain seperate Wheel datagram entries. Import RegEx module to make use of built in functions
    # 2. Iterate through all wheel entries and convert all wheel entries into inner lists that contain each data piece as a seperate element by splitting with more than one condition. Through this, only relevant data elements are stored as a seperate element in the wheel entry list and all newline or whitespace characters are disregarded
    # 3. Convert all wheel elements that are numbers to integers instead of leaving them as strings. This way, operations can be done on them later if needed
    # 4. Return the list containing all wheel entries 


# Time Complexity: O(3N), where N is the amount of characters in the file or the length of the contents of the file data given. Linear time complexity
import re
def parse_file(raw_wheel_data: str) -> list[list]:
    """"
    Seperates wheel entries in the file's contents and seperates each data piece by distinguishing from irrelevant characters. Returns the wheel entries as a list of seperate wheel entry lists
    """

    all_wheel_entries = re.split(r'\n\s*\n', raw_wheel_data)
    
    for idx in range(len(all_wheel_entries)):
        all_wheel_entries[idx] = re.split('   \n|  \n| \n|\n|   |  | ', all_wheel_entries[idx])

    for idx in range(len(all_wheel_entries)):
        for inner_idx in range(len(all_wheel_entries[idx])):
            if all_wheel_entries[idx][inner_idx].isdigit():
                all_wheel_entries[idx][inner_idx] = int(all_wheel_entries[idx][inner_idx])

    return all_wheel_entries
        

print(parse_file(file_contents))  # [['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '1', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '45', '4', '1', '1', '1', '3', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '200'], ['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '2', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '44', '4', '1', '1', '1', '4', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '199'], ['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '3', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '43', '4', '1', '1', '1', '5', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '198'], ['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '4', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '42', '4', '1', '1', '1', '6', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '197']]
            
        
               
    

        
    
        
