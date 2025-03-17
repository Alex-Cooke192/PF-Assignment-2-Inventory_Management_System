import config

class admin:
    def __init__(self):
        pass

    def screen_init(self, screen):
        self.interface = screen

    def fetch_inventory(self):
        inventories_name=self.interface.inventories_name_entry.get()
        if len(inventories_name) == 0: # Entry is empty so may have forgotten to input name
            response = messagebox.askyesno("Blank Name", "Name is empty, do you wish to proceed?")
            if response is False:
                return 0
        self.interface.inventories_name_entry_string.set("")
        print('The inventory is'+inventories_name)
        return inventories_name

    def fetch_item(self):
        inventory_name=self.interface.inventory_name_entry.get()
        item_name=self.interface.item_name_entry.get()
        quantity=self.interface.quantity_entry.get()
        if len(inventory_name) == 0 or len(item_name) == 0 or len(quantity) == 0: # One of the fields are empty
            response = messagebox.askyesno("Blank Field", "One or more fields are empty, do you wish to proceed?")
            if response is False:
                return 0
        try:
            quantity = int(quantity)
        except ValueError: 
            self.interface.execution_note_box.configure(state="normal")
            self.interface.execution_note_box.insert(tk.END, "\nFAIL:Quantity type not valid\n")
            self.interface.execution_note_box.configure(state="disabled")
        self.interface.inv_name.set("")
        self.interface.itm_name.set("")
        self.interface.enter_quantity.set("")
        return [inventory_name, item_name, quantity]
    
    def validate_inventory(self, inventory_name, inventories):
    # Function checks the 'inventories' dictionary to see if the dicntionary exists
    # If function returns true, name already exists, 
    # if it returns false, name doesnt exist
        name_check = False 
        for key, value in config.inventories.items():
            if key == inventory_name:
                name_check = True 
        if name_check == False:
            # Name doesnt exist
            print('Name doesnt exist')
            return 0
        elif name_check == True:
            # Name does exist
            print('Name does exist')
            return 1

    def validate_item(self, item_attr):
        name_check = False 
        for key, value in config.inventories.items():
            if key == item_attr[0]: # Item_attr[0] is inventory name
                name_check = True 
        if name_check == False:
            # Name doesnt exist
            print('Name doesnt exist')
            return 0
        elif name_check == True:
            item_check = False
            # Inventory name does exist
            print('Name does exist')
            ### Validate item name 
            for key in config.inventories[item_attr[0]]: 
                if key == item_attr[1]: # item_attr[1] is the item name
                    item_check = True 
            if item_check == True:
                # Item already exists - edit quantity
                return 11
            elif item_check == False: 
                # Item doesn't exist 
                return 10
