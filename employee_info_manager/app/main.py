import tkinter as tk 
from tkinter import ttk
import ui.main_window as wd
import db.connection as co




def main():
    root = tk.Tk()
    root.title("Employee Info Manager")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}+0+0")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font= ("Arial", 10, "bold"), foreground="#1f1f1f", background= "#d9d9d9")
    style.map("Treeview.Heading", background = [("active", "#e6e6e6")])
    
    #view
    menu = tk.Menu(root)
    root.config(menu= menu)
    file = tk.Menu(menu)
    menu.add_cascade(label= "File", menu=file)
    file.add_command(label="Export csv")


    #wight to choose database
    database = ttk.Combobox(root, values=["Employee Info Manager"], state= "readonly", font=("Arial", 20), width= 27, height= 3)
    database.place(x= 450, y =500)
    database.set("Database")

    def select(event):
        if database.get() == "Employee Info Manager" :
            wd.Window(root)
            database.destroy()
    database.bind("<<ComboboxSelected>>", select)

    
    co.cuu(root)


    root.mainloop()

if __name__ == "__main__":
    main()