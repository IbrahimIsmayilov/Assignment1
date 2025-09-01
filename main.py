#  Get as many files as the user would like to upload and convert them to EEPROM cartridge objects
#  Once converted, analyze all entries for all EEPROM cartridges and display the messages regarding all entries

import eeprom_class

def main():
    filename = input('Which file would you like to analyze?: ')
    user_choice = True
    user_files = [filename]
    EEPROM_Cartridges = []

    while user_choice == True:
        user_response = input("Would you like to upload more filenames?: Press Y for Yes and N for No: ")
        if user_response.lower() == 'y':
            filename = input('Please enter new filename: ')
            user_files.append(filename)
        else:
            user_choice = False

    for filename in user_files:
        EEPROM_Cartridges.append(eeprom_class.EEPROMCartridge(filename))
    
    for cartridge in EEPROM_Cartridges:
        cartridge.get_objects()
        cartridge.analyze_all_wheels_headers()
        cartridge.get_all_wheels_mini_entries()

        cartridge.check_all_wheels_region1_2s()
        cartridge.check_manufacturing_details()
        cartridge.check_part_ids()

        cartridge.analyze_all_wheels_ID()
        cartridge.analyze_all_wheels_regions()
        
        cartridge.return_str_all_wheels()


main()




        

        
    
    
    



        









    

