import mysql.connector
import tkinter as tk 
from tkinter import ttk


def cuu(root):
    
    tk.Label(root, text="Host",font=("Arial", 20)).place(x= 450, y= 100)
    tk.Label(root, text="User",font=("Arial", 20)).place(x= 450, y= 200)
    tk.Label(root, text= "Password",font=("Arial", 20)).place(x= 450, y= 300)
    host = tk.Entry(root, font= ("Arial",20))
    host.place(x= 580, y= 100)
    user = tk.Entry(root, font= ("Arial",20))
    user.place(x= 580, y= 200)
    password = tk.Entry(root, font=("Arial", 20))
    password.place(x= 580, y= 300)
    
    tk.Button(root, text="Connecting", command= lambda: set_connection_info(host.get(), user.get(), password.get()), bg= "#D3D3D3",font= ("Arial",15), width= 39).place(x= 450, y= 400)
    

DB_HOST = None
DB_USER = None
DB_PASSWORD = None

def set_connection_info(host, user, pwd):
    global DB_HOST, DB_USER, DB_PASSWORD
    DB_HOST = host
    DB_USER = user
    DB_PASSWORD = pwd


def get_connection():
    return mysql.connector.connect(
           host=DB_HOST,
           user=DB_USER,
           password= DB_PASSWORD,  # thay bằng mật khẩu thật của root
           database="Employee_Information_Manager"
    )

    