# Inventory Management System
# 12.02.2025
 
 class Asset: 
     def __init__(self, asset_id, name, quantity):
         self.asset_id = asset_id
         self.name = name
         self.quantity = quantity
         
     def edit_quantity(self, new_quantity):
         self.quantity = new_quantity
         print('Object', self.name, 'quantity changed to', self.quantity)
 
 class inventory_manager(): 
     def __init__(self):
         self.inventory = []
     def add_asset(self, asset):
         self.inventory.append(asset)
     def remove_asset(self, asset):
         self.inventory.remove(asset) 
 
 
 class GUI():
     # Each button is a different function
     pass 
        
 
 def main():
     print ('Inventory Management System: Ver 0.1')
     print('1. Create inventory')
     print('2. Exit System')
 
     command = False
     while command == False: 
         try:
             option = int(input('Enter option num:'))
         except ValueError:
             print('Data not of valid type, enter again.')
         if option == 1:
             inventory_name = input('Inventory Name: ')
              = inventory_manager()
             print(Warehouse.inventory)
             # Display inventory
             pass
         elif option == 2:
             # Exit inventory
             command = True
 
 main()
