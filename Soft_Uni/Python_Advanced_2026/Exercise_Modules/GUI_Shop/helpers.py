import tkinter as tk
import os

from canvas import app

base_folder = os.path.dirname(__file__)

def clear_screen():
    for el in app.grid_slaves():
        el.destroy()

def get_current_user():
    with open(base_folder + "\\db\\current_user.txt") as file:
        return file.read().strip()