# Inventories manager class
# This file deals with adding/removing dta from the 'inventories' dictionary
# And posting relevant comments to the GUI, such as status updates

import config
import tkinter as tk

class inventories_manager: 
    def __init__(self):
        self.counter = 0 # tracks how many inventories are active in the dictionary
        self.new_inventory_ID = 0
    def interface_init(self, screen):
        self.interface = screen
    
    def add_inventory(self, inventories, inventory_name, inventory_flag):
        self.new_inventory_ID += 1
        self.counter += 1
        if inventory_flag == 0: # Name doesn't exists so new inventory CAN be created
            self.interface.execution_note(function_name="\'Add inventory\'", execution_flag=True)
            inventories[inventory_name] = {}
        elif inventory_flag == 1: # Name already exists, cannot create new inventory
            self.interface.execution_note(function_name="\'Add inventory\'", execution_flag=False)

    def remove_inventory(self, inventories, inventory_name, inventory_flag):
        if len(inventories) == 0:
            self.interface.execution_note(function_name="\'Remove inventory\'", execution_flag=False)
            self.interface.execution_note_box.configure(state="normal")
            self.interface.execution_note_box.insert(tk.END, "\nNo inventories exist\n")
            interface.execution_note_box.configure(state="disabled")
            return 0
        if inventory_flag == 0: # Name doesnt exist so cannot be removed
            self.interface.execution_note(function_name="\'Remove inventory\'", execution_flag=False)
        elif inventory_flag == 1: # Name does exist so can be removed
            self.interface.execution_note(function_name="\'Remove inventory\'", execution_flag=True)
            del inventories[inventory_name] # Remove inventory from data
        self.counter -= 1

    def display_inventory(self, inventories, inventory_name, inventory_flag):
        # Check if any inventories exist
        if len(inventories) == 0:
            self.interface.execution_note(function_name="\'Display inventory\'", execution_flag=False)
            self.interface.execution_note_box.configure(state="normal")
            self.interface.execution_note_box.insert(tk.END, "\nNo inventories exist\n")
            self.interface.execution_note_box.configure(state="disabled")
            return 0
        if inventory_flag == 0: # Name doesnt exist so cannot be displayed
            self.interface.execution_note(function_name="\'Display inventory\'", execution_flag=False)
            ##### OPTION TO ADD INVENTORY INSTEAD
        elif inventory_flag == 1: # Name does exist so can be displayed
            self.interface.execution_note(function_name="\'Display inventory\'", execution_flag=True)
            # Print inventory to inventory box on the GUI
            self.interface.inventory_box.configure(state="normal")
            self.interface.inventory_box.insert(tk.END, "--------------------------------------")
            self.interface.inventory_box.insert(tk.END, "\n" + inventory_name + "\n \n")
            for key, value in inventories[inventory_name].items():
                self.interface.inventory_box.insert(tk.END, key + ": " + str(value) + "\n")
            self.interface.inventory_box.insert(tk.END, "--------------------------------------\n")
            self.interface.inventory_box.configure(state="disabled")
        self.counter -= 1
    
    def display_all(self, inventories):
            if len(inventories) == 0:
                self.interface.inventory_box.insert(tk.END, "EMPTY\n")
                return 0
        # Display all inventories
            for name, inventory in inventories.items():
                self.interface.inventory_box.insert(tk.END, name + ":\n")
                # print("\ninventory:", name)
                for key in inventory:
                    self.interface.inventory_box.insert(tk.END, "\t- " + key + ":" + str(inventory[key]) + '\n')

    def remove_all(self, inventories):
        inventories = {}
        self.interface.inventory_box.insert(tk.END, "EMPTY\n")

    def add_item(self, item_flag, item_attr):
        inventory_name = item_attr[0]
        item_name = item_attr[1]
        quantity = item_attr[2]
        if item_flag == 0: # Inventory name doesnt exist so cannot be added 
            self.interface.execution_note(function_name="\'Add item\'", execution_flag=False)
        elif item_flag == 10: # Inventory exists but item doesnt so add new item to list 
            self.interface.execution_note(function_name="\'Add item\'", execution_flag=True)
            config.inventories[inventory_name][item_name] = quantity 
        elif item_flag == 11: # Inventory exists and item already exists so edit quantity
            self.interface.execution_note(function_name="\'Add item\'", execution_flag=True)
            config.inventories[inventory_name][item_name] += quantity 
    
    def remove_item(self, item_flag, item_attr):
        inventory_name = item_attr[0]
        item_name = item_attr[1]
        quantity = item_attr[2]
        if item_flag == 0: # Inventory name doesnt exist so cannot be added 
            self.interface.execution_note(function_name="\'Remove item\'", execution_flag=False)
        elif item_flag == 10: # Inventory exists but item doesnt so cannot be removed
            self.interface.execution_note(function_name="\'Remove item\'", execution_flag=False)
        elif item_flag == 11: # Inventory exists and item exists so can be removed
            self.interface.execution_note(function_name="\'Remove item\'", execution_flag=True)
            config.inventories[inventory_name][item_name] -= quantity 
