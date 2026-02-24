import json
import tkinter as tk
import os
from PIL import Image, ImageTk

from canvas import app
from helpers import clear_screen, get_current_user

base_folder = os.path.dirname(__file__)

def update_current_user(username, product_id):
    with open(base_folder + "\\db\\users.txt", "r+") as file:
        users = [json.loads(u.strip()) for u in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(usr) + "\n" for usr in users])
                return
            
def purchase_product(product_id):
    with open(base_folder + "\\db\\products.txt", "r+") as file:
        products = [json.loads(p.strip()) for p in file]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(pp) + "\n" for pp in products])
                return

def buy_product(product_id):
    clear_screen()

    username = get_current_user()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)
    
    render_products_screen()


def render_products_screen():
    clear_screen()

    with open(base_folder + "\\db\\products.txt") as file:
        products = [json.loads(line.strip()) for line in file]
        products = [p for p in products if p["count"] > 0]
        products_per_line = 3
        rows_for_product = len(products[0])

        for i, product in enumerate(products):
            row = i // products_per_line * rows_for_product
            column = i % products_per_line

            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, "db\\images", product["img_path"])).resize((228, 228))
            photo_img = ImageTk.PhotoImage(img)
            image_label = tk.Label(app, image=photo_img)
            image_label.image = photo_img
            image_label.grid(row=row+1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row+2, column=column)

            tk.Button(app, text=f"Buy {product['name']}", command=lambda p=product["id"]: buy_product(p)).grid(row=row+3, column=column)