#  This class will be the parent class of the wheel class and contain properties that should be expected among all classes

class EntryDatagram:
    def __init__(self, entry_data):
        self.all_data = entry_data
        self.valid_data = True
        self.object_type = 'Unidentified Object'