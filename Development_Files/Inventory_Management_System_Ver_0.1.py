# Inventory Management System
# 12.02.2025

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

with open("inventoryFile.txt", "w") as file:
    file.write('text')

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
        print(inventory_name, 'contains\n', self.inventory)

    def add_asset(self, inventory_name, asset):
        self.inventory.append(asset)

    def remove_asset(self, asset):
        self.inventory.remove(asset)


class inventories_manager: 
    def __init__(self):
        self.counter = 0 # tracks how many inventories are active in the dictionary
    
    def add_inventory(self, inventories):
        self.counter += 1
        inventory_name = input("Inventory name: ").strip()
        # Validate name exists
        name_check = False 
        while name_check == False:
            name_check = True
            for key, value in inventories.items():
                if key == inventory_name:
                    name_check = False 
            if name_check == False:
                print('Name already taken')
                inventory_name = input("Enter new name: ").strip()
        inventories[inventory_name] = {}

    def delete_inventory(self, inventories):
        if len(inventories) == 0:
            print('Cannot delete inventory - no inventories exist!') 
            return 0
        inventory_name = input("Enter name of inventory to delete:").strip() 
        # Verify name exists 
        del inventories[inventory_name]
        self.counter -= 1

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

def logout():
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response:
        root.destroy()  # Close the application window
    # write relevant text to file # Destroy GUI
                
manager = inventories_manager()
inventories = {}

### GUI Functions
# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1000x666")

# Delare string variable for storing name of inventory to add
inventory_name = tk.StringVar()

# Create a label widget
label = tk.Label(root, text="Inventory Management System", font=("Arial", 14))
label.pack(pady=20)

# Create 'add inventory' button 
add_inventory_button = tk.Button(root, 
                    text="Add Inventory", 
                    command=lambda: manager.add_inventory(inventories)).place(x=30, y=80)

# Add box to enter inventory names
name_label = tk.Label(root, text='Inventory Name', font=("Arial", 10))

name_entry = tk.Entry(root, 
                      textvariable = inventory_name)
name_label.place(x=70, y=80)
name_entry.place(x=80, y=100)

# Remove inventory button
remove_inventory_button = tk.Button(root, 
                   text="Delete Inventory",
                   command=lambda: manager.delete_inventory(inventories)).place(x=30, y=120)

# Read BAE logo image and format to the right size
BAES_logo = PhotoImage(file="C:/Users/alexa/OneDrive/Documents/B&FC Year 1/Programming Fundamentals/Assignment 2 inventory management system/bae-systems-logo.png")
BAES_logo = BAES_logo.subsample(4,4)

# Create label to display BAE logo & add to GUI 
BAE_logo_label = tk.Label(root, image=BAES_logo).place(x = 750, y = 0)

# Create 'logout' button & add to GUI 
logout_button = tk.Button(root, text = 'Logout', command = logout).place(x = 800, y= 600)

def enter_inventory_name_screen():
    inventory_name = tk.StringVar()
    # initialise the screen
    name_popup = tk.Tk()
    name_popup.title('Enter Inventory name')
    name_popup.geometry("300x200")

    # Add entry for inventory name
    name_entry = tk.Entry(name_popup, textvariable=inventory_name)
    name_entry.pack(fill='x', expand=True)
    name_entry.focus()

    # submit button
    submit_button = tk.Button(name_popup, text = "submit", command = name_popup.destroy)

def submit_clicked():
    pass

# Start the Tkinter event loop
root.mainloop()

# Just an idea: 
# def validate_inventory_name():

       
def main():
    ## file = open("inventoryFile.txt", "r")
    # Immediately create the manager
    ########## manager = inventories_manager()
    ########## inventories = {}
    print('Inventory Management System: Ver 0.1')
    print('1. Create inventory')
    print('2. Display inventory')
    print('3. Edit inventory')
    print('4. Enter function here')
    print('5. Delete inventory')
    print('6. Display all inventories')
    print('7. Exit System')
    command = False
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
            manager.add_inventory(inventories)
        elif option == 2: 
            # Display inventory
            manager.display_inventory(inventories)
        elif option == 3:
            # edit inventory 
            # This will involve the 'inventory_manager' class
            inventory_name = input("Enter name of inventory to edit: ")
            inv = inventories[inventory_name]
            print('1. Add item to inventory')
            print('2.Remove item from inventory')
            edit_option = input('Enter option: ')

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
