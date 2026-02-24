import json
import tkinter as tk
import os

from canvas import app
from helpers import clear_screen
from products import render_products_screen

base_folder = os.path.dirname(__file__)

def login(username, password):
    with open(base_folder + "\\db\\user_credentials.txt") as f:
        for line in f:
            user, pwd = line.strip().split(", ")
            if user == username and pwd == password:
                with open(base_folder + "\\db\\current_user.txt", "w") as file:
                    file.write(username)
                render_products_screen()
                return
    render_login_screen("Invalid username or password!")
    

def render_login_screen(error=None):
    clear_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app, show="*")
    password.grid(row=1, column=0)

    tk.Button(
        app,
        text="Enter",
        fg="black",
        bg="green",
        command=lambda: login(username.get(), password.get())
    ).grid(row=2, column=0)

    if error:
        tk.Label(
            app,
            text=error,
            fg="red",
        ).grid(row=3, column=0)

def register(**user):
    user.update({"products": []})
    with open(base_folder + "\\db\\user_credentials.txt", "r+") as file:

        users = [line.strip().split(", ")[0] for line in file]

        if user["username"] in users:
            render_register_screen(error="Username already exists")
            return
        file.write(f"{user['username']}, {user['password']}\n")
    
    with open(base_folder + "\\db\\users.txt", "a") as file:
        file.write(json.dumps(user) + "\n")

    render_login_screen()

def render_register_screen(error=None):
    clear_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    tk.Button(
        app,
        text="Register",
        fg="black",
        bg="green",
        command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(), last_name=last_name.get())
    ).grid(row=4, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=5, column=0)


def render_main_enter_screen():
    clear_screen()

    tk.Button(
        app,
        text="Login",
        fg="white",
        bg="green",
        command=render_login_screen
    ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Register",
        fg="black",
        bg="yellow",
        command=render_register_screen
    ).grid(row=0, column=1)