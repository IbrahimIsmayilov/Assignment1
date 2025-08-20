# 1. Develop a function to read file from given file and return the contents
# 2. Develop a function to parse the contents of the file and place them in seperate elements

# 1. 
    # 1. Reads the file and returns the contents stored in a variable


# Time Complexity: O(N), where N is the amount of characters in the file or the length of the file. Linear time complexity
def read_file(filename: str) -> list:
    with open(filename) as file:
        raw_wheel_data = file.read()

    return raw_wheel_data

file_contents = read_file('colleague-file.log')


# 2. 
    # 1. Create variables that store both letters and numbers to be used when checking characters of the file's contents
    # 2. Create a new list that will store all wheel entries seperately and return it at the end
    # 3. Create a new list for wheel entries and a variable to differentiate between seperate digits and larger numbers
    # 4. Iterate through the contents of the file and seperate the wheel entries that will only contain relevant characters (no whitespace or newline)
    # 5. Return the list containing all the entries 


# Time Complexity: O(N), where N is the amount of characters in the file or the length of the file. Linear time complexity
import string
def parse_file(raw_wheel_data: str) -> list:
    numbers = '1234567890'
    letters = string.ascii_letters

    all_wheel_entries = []
    wheel_entry = []
    wheel_num = ''

    for idx in range(len(raw_wheel_data)):
        if raw_wheel_data[idx:idx + 2] == '\n\n' and len(wheel_entry) != 0:
            all_wheel_entries.append(wheel_entry)
            wheel_entry = []

        if raw_wheel_data[idx] in numbers:
            wheel_num += raw_wheel_data[idx]
            if idx != len(raw_wheel_data) - 1 and raw_wheel_data[idx + 1] not in numbers:
                wheel_entry.append(wheel_num)
                wheel_num = ''

        elif raw_wheel_data[idx] in letters:
            wheel_entry.append(raw_wheel_data[idx])

    all_wheel_entries.append(wheel_entry)

    return all_wheel_entries
            

print(parse_file(file_contents))  # [['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '1', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '45', '4', '1', '1', '1', '3', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '200'], ['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '2', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '44', '4', '1', '1', '1', '4', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '199'], ['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '3', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '43', '4', '1', '1', '1', '5', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1', '198'], ['9', '37', '0', '0', '0', '0', '0', '0', '210', '8', '2', '0', '0', '8', '13', '4', '0', '0', '6', 'W', 'h', 'e', 'e', 'l', '4', '6', 'O', 't', 't', 'a', 'w', 'a', '6', 'C', 'a', 'n', 'a', 'd', 'a', '42', '4', '1', '1', '1', '6', '9', '8', '2', '4', '8', '1', '5', '3', '5', '1']]
            
        
               
    

        
    
        
