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
     
     def edit_value(self, new_value):
         self.value = new_value
         print('Object', self.name, 'value changed to', new_value)
 
 
 class inventory_manager(): 
     def __init__(self, inventory_name):
         self.name = inventory_name
         self.inventory = {}
         pass
         print(inventory_name, 'contains\n', self.inventory)
 
     def add_asset(self, asset):
     def add_asset(self, inventory_name, asset):
         self.inventory.append(asset)
 
     def remove_asset(self, asset):
         self.inventory.remove(asset) 
 
     def display_inventory(self):
         for asset in self.inventory(0, len(self.inventory)-1):
             print(asset) 
         self.inventory.remove(asset)
 
 
 class inventories_manager: 
     def __init__(self):
         self.inventories = {}
         self.counter = 0
         self.counter = 0 # tracks how many inventories are active in the dictionary
 
     def add_inventory(self, inventories):
         self.counter += 1
         inventory_name = input("Inventory name: ")
         inventory_name = input("Inventory name: ").strip()
         # for loop checks if the entered name of the inventory already exists
         name_check = False 
         while name_check == False:
 @@ -46,42 +45,96 @@
                     name_check = False 
             if name_check == False:
                 print('Name already taken')
                 inventory_name = input("Enter new name: ")
     
         inv = inventory_manager(inventory_name)
         self.inventories.update({inventory_name:self.counter})
         print(self.inventories)
                 inventory_name = input("Enter new name: ").strip()
         inventories[inventory_name] = {}
 
     def remove_inventory(self): 
     def delete_inventory(self, inventories):
         if len(inventories) == 0:
             print('Cannot delete inventory - no inventories exist!') 
             return 0
         inventory_name = input("Enter name of inventory to delete:").strip() 
         # Verify name exists 
         del inventories[inventory_name]
         self.counter -= 1
         pass 
 
     def display_inventory(self, inventories):
         # Check if any inventories actually do exist 
         if len(inventories) == 0:
             print('Cannot display inventory - no inventories exist!') 
             return 0
         inventory_name = input('Enter name of inventory to display:').strip()
         # Verify name exists
         search = False # False as the inventory hasnt been found
         while search == False: 
             search = True
             try: 
                 print(inventory_name, ": ", inventories[inventory_name])
             except KeyError:
                 search = False
                 print("Inventory does not exist, enter new name")
                 print("Enter \'Stop\' if you no longer want to display an inventory")
                 inventory_name = input('Enter name of inventory to display:').strip()
                 if inventory_name == 'Stop': 
                     search = True
                     return 0 
 
 class GUI():
     # Each button is a different function
     pass 
 
 def main():
     ## file = open("inventoryFile.txt", "r")
     # Immediately create the manager
     manager = inventories_manager()
     print ('Inventory Management System: Ver 0.1')
     inventories = {}
     print('Inventory Management System: Ver 0.1')
     print('1. Create inventory')
     print('2. Display inventory')
     print('3. Exit System')
     print('3. Edit inventory')
     print('4. Enter function here')
     print('5. Delete inventory')
     print('6. Display all inventories')
     print('7. Exit System')
     command = False
     while command == False: 
         try:
             option = int(input('Enter option num:'))
         except ValueError:
             print('Data not of valid type, enter again.')
     while command == False:
         check_flag = False 
         while check_flag == False:
             # Data validation to check the option entered is valid 
             check_flag = True
             try:
                 option = int(input('Enter option num:'))
             except ValueError:
                 check_flag = False 
                 print('Data not of valid type, enter again.')
                 option = int(input('Enter option num:'))
             # if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6 and option != 7:
             if option < 1 and option > 7: 
                 check_flag = False
                 print('Number given is not an option, enter again')
         if option == 1:
             # Create inventory
             obj = manager.add_inventory(manager.inventories)
             manager.add_inventory(inventories)
         elif option == 2: 
             # Display inventory
             manager.display_inventory(): 
 
             manager.display_inventory(inventories)
         elif option == 3:
             # edit inventory 
             pass
         elif option == 4:
             pass 
         elif option == 5:
             # Delete inventory
             manager.delete_inventory(inventories)
         elif option == 6:
             # Display all inventories
             for key in inventories:
                 name = key 
                 print(name, ":",)
                 for key in inventories[key]:
                     # Print the asset name & quantity
                     print('frog')
         elif option == 7:
             # Exit inventory
             command = True
             # Write dictionary to file
 main()
