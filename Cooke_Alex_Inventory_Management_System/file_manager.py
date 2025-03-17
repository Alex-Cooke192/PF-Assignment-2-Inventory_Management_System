# File manager class
# This class writes and reads the contents of inventories
# to and from a text file

import os
import config
import json

class file_object:
    def __init__(self):
        self.inventories = {}
    def file_write_inventories(self, inventories):
        file_exists = os.path.exists('./inventories_file.txt')
        with open('./inventories_file.txt', 'w') as file:
            json.dump(inventories, file)

    def file_read_inventories(self, inventories):
        file_exists = os.path.exists('./inventories_file.txt')
        if file_exists == True:
            # Read data from the file
            with open('./inventories_file.txt', 'r') as file:
                data = file.read()
            
            # Reformat as a dictionary
            try:
                temp = json.loads(data)
            except json.decoder.JSONDecodeError:
                pass
            print(type(inventories), inventories)
        return temp
