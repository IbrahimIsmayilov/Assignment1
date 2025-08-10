# 1. Develop a function to read file from given file which EEPROM data and contain seperate wheel components. 
# 2. Develop a function that begins to parse using by dividing the data into section. For every wheel componenet, there are 3 sections. Each section ends with a checksum padding and a new one begins after up until the third section. Within each of these 3 main sections, each section has a preset amount of mini sections. The first section is called the header and consists of itself. The second section has 4 mini-sections. This includes the date, wheel id, city and country mini-components followed by a checksum phadding. The third and last section has 2 mini components called tray id and part id, which are also followed by the checksum padding. The function must return a boolean value if the cartidges have the correct data and a string otherwise that indicates where each error may be. The function must meet many requirements such as:
#           - Calculating the checksums wherever possible, at the end of each of the 3 main sections that contain a checksum padding. 
#           - Printing each possible mini-component's data of the wheel on a new line for clarity.
#           - Returning a boolean value if the cartidges have the correct data and a string otherwise that indicates where the error is located, in terms of which section or mini-entry.  

# 1
    # 1. Create a list to store all wheel componenets
    # 2. Read the file in python
    # 3. Divide all wheel data components into seperate string elements and store them in the created list. 
    # 4. Return the list-

def read_wheel_data(filename: str) -> list:
    wheel_data_components = []
    
