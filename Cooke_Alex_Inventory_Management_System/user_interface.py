# User interface class
# Makes the user interface & all widgets 

import tkinter as tk
from tkinter import messagebox, PhotoImage, scrolledtext, font
import os
from datetime import datetime
import config


class GUI(tk.Tk):
    def __init__(self, peripheral_manager, brain, file_bus):
        super().__init__()
        # Set up main application window
        self.title("Inventory Management System")
        self.geometry("1000x666")

        self.app_manager = peripheral_manager
        self.manager = brain
        self.file_manager = file_bus

        title_font = font.Font(weight="bold", size=16, family="Comic Sans MS")

        # Initialise memeory space for entry boxes
        self.inventories_name_entry_string = tk.StringVar()
        self.inv_name = tk.StringVar()
        self.itm_name = tk.StringVar()
        self.enter_quantity = tk.IntVar()

        # Create title label widget
        self.label = tk.Label(self, text="Inventory Management System", font=title_font)
        self.label.place(relx=0.34, rely=0, relwidth=0.33, relheight=0.1)
        ### self.label.pack(pady=30, anchor=tk.N)

        # Read BAE logo image and format to the right size
        directory = os.getcwd()
        # for images in os.listdir(os.getcwd()):
        image_path = (f'{directory}/BAE_Systems_logo.png')
        self.BAES_logo = PhotoImage(file=image_path)
        self.BAES_logo = self.BAES_logo.subsample(3,4)

        # Create label to display BAE logo & add to GUI 
        self.BAE_logo_label = tk.Label(self, image=self.BAES_logo).place(relx=0.67,rely=0, relwidth=0.33, relheight=0.1)
        # pack(anchor=tk.NE)

        button_text = font.Font(font='Helvetica', size=10)

        # Create 'add inventory' button widget
        self.add_inventory_btn = tk.Button(self, text="Add inventory", font=button_text, command=lambda:self.add_inventory_clicked(config.inventories))
        self.add_inventory_btn.place(relx=0.04, rely= 0.12, relwidth=0.26)

        # Create 'Remove inventory' button widget
        self.remove_inventory_btn = tk.Button(self, text="Remove inventory", font=button_text, command=lambda:self.remove_inventory_clicked(config.inventories))
        self.remove_inventory_btn.place(relx=0.04, rely=0.21, relwidth=0.262)

        # Create 'Display inventory' button widget
        self.display_inventory_btn = tk.Button(self, text="Display inventory", font=button_text, command=lambda:self.display_inventory_clicked(config.inventories))
        self.display_inventory_btn.place(relx=0.04, rely = 0.30, relwidth=0.262)

        # Create 'add item' button widget
        self.add_item_btn = tk.Button(self, text='Add item to inventory', font=button_text, command=lambda: self.add_item_clicked(config.inventories))
        self.add_item_btn.place(relx=0.369, rely=0.57, relwidth=0.262)

        # Create 'remove item' button widget
        self.remove_item_btn = tk.Button(self, text='Remove item from inventory', font=button_text, command=lambda: self.remove_item_clicked(config.inventories))
        self.remove_item_btn.place(relx=0.369, rely=0.66, relwidth=0.262)

        # Create 'display all' button widget
        self.display_all_btn = tk.Button(self, text="Display all", font = button_text, command=lambda: self.display_all_clicked(config.inventories))
        self.display_all_btn.place(relx=0.04, rely=0.57, relwidth=0.262)

        # Create 'remove all' button widget
        self.remove_all_btn = tk.Button(self, text="Remove all", font = button_text, command=lambda: self.remove_all_clicked(config.inventories))
        self.remove_all_btn.place(relx= 0.04, rely = 0.1, relwidth=0.262)

        # Create 'logout button' and add to UI 
        self.logout_btn = tk.Button(self, text="Logout", font=button_text, command=self.logout).place(relx=0, rely=0)

        # Create inventories name label and entry for add inventory, remove inventory and display inventory functions
        self.inventories_name_entry_label = tk.Label(self, text="Inventory name:", font=button_text)
        self.inventories_name_entry_label.place(relx=0.02, rely=0.44, relwidth=0.12)

        # Create inventories name entry for add inventory, remove inventory, and display inventory
        self.inventories_name_entry = tk.Entry(self, textvariable=self.inventories_name_entry_string, justify="center")
        self.inventories_name_entry.place(relx=0.15, rely=0.45, relwidth=0.16)

        ### Create item add/remove boxes (This includes inventory name, item name and quantity)
        # Create inventory name entry and label 
        self.inventory_name_entry_label = tk.Label(self, text="Inventory name:", font=button_text, justify="right")
        self.inventory_name_entry_label.place(relx=0.35, rely=0.25, relwidth=0.12)
        self.inventory_name_entry = tk.Entry(self, textvariable=self.inv_name, font=button_text)
        self.inventory_name_entry.place(relx=0.46, rely=0.25, relwidth=0.17)

        # Create item name entry and label 
        self.item_name_entry_label = tk.Label(self, text="Item name:", font=button_text, justify="right")
        self.item_name_entry_label.place(relx=0.35, rely=0.30, relwidth=0.12)
        self.item_name_entry = tk.Entry(self, textvariable=self.itm_name, font=button_text)
        self.item_name_entry.place(relx=0.46, rely=0.30, relwidth=0.17)

        # Create quantity entry and label
        self.quantity_entry_label = tk.Label(self, text="Quantity:", font=button_text, justify="right")
        self.quantity_entry_label.place(relx=0.35, rely=0.35, relwidth=0.12)
        self.quantity_entry = tk.Entry(self, textvariable=self.enter_quantity, font=button_text)
        self.quantity_entry.place(relx=0.46, rely=0.35, relwidth=0.17)

        # Create Scrolling text box for execution messages
        self.execution_note_box = scrolledtext.ScrolledText(self,wrap=tk.WORD,width=40,height=10)
        self.execution_note_box.configure(state ='disabled')
        self.execution_note_box.place(relx=0.005,rely=0.70,relwidth=0.33,relheight=0.29)
        # Set focus to the text area
        self.execution_note_box.focus()

        # Create font style for label for execution box - what a mouthful! 
        execution_box_label_font = font.Font(family="Comic Sans MS",size=12,weight="bold")

        # Create label for execution box
        self.execution_box_label = tk.Label(self, text="Command state updates",justify="center", font=execution_box_label_font)
        self.execution_box_label.place(relx=0, rely=0.65, relheight=0.05, relwidth=0.33)

        # Create Scrolling text box for displaying inventories
        self.inventory_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=10, height=40)
        self.inventory_box.configure(state ='disabled')
        self.inventory_box.place(relx=0.67, rely=0.09, relwidth=0.33, relheight=0.9)
        # Set focus to the text area 
        self.inventory_box.focus()

# ============================================================================================================================

    def logout(self):
        # Close the application window 
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.file_manager.file_write_inventories(config.inventories) # Write data to file
            self.destroy() 
    
    def add_inventory_clicked(self, inventories):
        inventories_name = self.app_manager.fetch_inventory() # Get inventory name to add from entry 
        # Validate inventory name
        inventories_flag = self.app_manager.validate_inventory(inventories_name, inventories)
        self.manager.add_inventory(inventories, inventories_name, inventories_flag)

    def remove_inventory_clicked(self, inventories):
        # Get inventory name from entry
        inventories_name = self.app_manager.fetch_inventory()  
        # Validate inventory name 
        inventories_flag = self.app_manager.validate_inventory(inventories_name, inventories)
        self.manager.remove_inventory(inventories, inventories_name, inventories_flag)

    def display_inventory_clicked(self, inventories):
        # Get inventory name from entry 
        inventories_name = self.app_manager.fetch_inventory() 
        # Validate inventory name
        inventories_flag = self.app_manager.validate_inventory(inventories_name, inventories)
        self.manager.display_inventory(inventories, inventories_name, inventories_flag)

    def display_all_clicked(self, inventories):
        self.inventory_box.configure(state="normal")
        self.manager.display_all(config.inventories)
        self.inventory_box.configure(state="disabled")
        self.execution_note(function_name="\'Display all\'", execution_flag=True)

    def remove_all_clicked(self, inventories):
        self.inventory_box.configure(state="normal")
        self.manager.remove_all(config.inventories)
        self.inventory_box.configure(state="disabled")
        self.execution_note(function_name="\'Remove all\'", execution_flag=True)
    
    def add_item_clicked(self, inventories):
        item_attr = self.app_manager.fetch_item()
        print('diowwef', item_attr)
        item_flag = self.app_manager.validate_item(item_attr)
        self.manager.add_item(item_flag, item_attr)

    def remove_item_clicked(self, inventories):
        item_attr = self.app_manager.fetch_item()
        item_flag = self.app_manager.validate_item(item_attr)
        self.manager.remove_item(item_flag, item_attr)

    def execution_note(self, function_name, execution_flag):
        # Displays execution note in execution note box, depending on 
        # if the fucntion sucessfully executed or not
        current_time = datetime.now()
        if execution_flag == True:
            self.execution_note_box.configure(state = "normal")
            self.execution_note_box.insert(tk.END, current_time)
            self.execution_note_box.insert(tk.END,"\nFunction:" + function_name + " SUCCESS.\n")
            self.execution_note_box.insert(tk.END,"==================================================\n")
            self.execution_note_box.configure(state = "disabled")
        elif execution_flag == False:
            self.execution_note_box.configure(state="normal")
            self.execution_note_box.insert(tk.END, current_time)
            self.execution_note_box.insert(tk.END,"\nFunction:" + function_name + " FAIL.\n")
            self.execution_note_box.insert(tk.END,"==================================================\n")
            self.execution_note_box.configure(state = "disabled")
            # Print reason for failure - depends on the function being executed
            if function_name == "\'Add inventory\'":
                self.execution_note_box.configure(state = "normal") # Open execution box - can be written to
                self.execution_note_box.insert(tk.END, "\nInventory already exists")
                self.execution_note_box.configure(state="disabled") # Close execution box - READ ONLY MODE
            elif function_name == "\'Remove inventory\'":
                self.execution_note_box.configure(state="normal")
                self.execution_note_box.insert(tk.END, "\nInventory does not exist\n")
                self.execution_note_box.configure(state="disabled")
            elif function_name == "\'Display inventory\'":
                self.execution_note_box.configure(state="normal")
                self.execution_note_box.insert(tk.END, "\nInventory does not exist\n")
                self.execution_note_box.configure(state="disabled")

# =======================================================================================================================

