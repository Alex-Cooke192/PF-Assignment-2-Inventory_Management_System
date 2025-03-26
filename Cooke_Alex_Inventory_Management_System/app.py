# import libraries
import tkinter as tk
from tkinter import messagebox, PhotoImage, scrolledtext, font
import pathlib
import json
import time
import os
import sys

from datetime import datetime

# Import other classes from files
from user_interface import GUI
from admin_manager import admin
from file_manager import file_object
from inventories_manager import inventories_manager
import config

directory = os.getcwd()
login_path = (f'{directory}/Login_System')
print(login_path)
sys.path.insert(0, login_path)

import LoginSystem

def grant_access():
    # Create objects & relevant pathways between objects
    app_manager = admin()
    manager = inventories_manager()
    file_manager = file_object()
    interface = GUI(app_manager, manager, file_manager)
    manager.interface_init(interface)
    app_manager.screen_init(interface)
    try: 
        config.inventories = file_manager.file_read_inventories(config.inventories)
    except UnboundLocalError:
        pass
    print(config.inventories)
    interface.mainloop() 
