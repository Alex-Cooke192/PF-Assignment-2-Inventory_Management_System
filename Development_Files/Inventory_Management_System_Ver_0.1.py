# Inventory Management System
# 12.02.2025
class Asset: 
    def __init__(self, asset_id, name, quantity, value):
        self.asset_id = asset_id
        self.name = name
        self.quantity = quantity
        self.value = value
        
    def edit_quantity(self, new_quantity):
        self.quantity = new_quantity
        print('Object', self.name, 'quantity changed to', self.quantity)


class inventory_manager(): 
    def __init__(self, inventory_name):
        self.name = inventory_name
        self.inventory = {}
        pass

    def add_asset(self, asset):
        self.inventory.append(asset)

    def remove_asset(self, asset):
        self.inventory.remove(asset) 

    def display_inventory(self):
        for asset in self.inventory(0, len(self.inventory)-1):
            print(asset) 


class inventories_manager: 
    def __init__(self):
        self.inventories = {}
        self.counter = 0
    
    def add_inventory(self, inventories):
        self.counter += 1
        inventory_name = input("Inventory name: ")
        # for loop checks if the entered name of the inventory already exists
        name_check = False 
        while name_check == False:
            name_check = True
            for key, value in inventories.items():
                if key == inventory_name:
                    name_check = False 
            if name_check == False:
                print('Name already taken')
                inventory_name = input("Enter new name: ")
    
        inv = inventory_manager(inventory_name)
        self.inventories.update({inventory_name:self.counter})
        print(self.inventories)

    def remove_inventory(self): 
        self.counter -= 1
        pass 


class GUI():
    # Each button is a different function
    pass 
       
def main():
    # Immediately create the manager
    manager = inventories_manager()
    print ('Inventory Management System: Ver 0.1')
    print('1. Create inventory')
    print('2. Display inventory')
    print('3. Exit System')
    command = False
    while command == False: 
        try:
            option = int(input('Enter option num:'))
        except ValueError:
            print('Data not of valid type, enter again.')
        if option == 1:
            # Create inventory
            obj = manager.add_inventory(manager.inventories)
        elif option == 2: 
            # Display inventory
            manager.display_inventory(): 

        elif option == 3:
            # Exit inventory
            command = True
main()
