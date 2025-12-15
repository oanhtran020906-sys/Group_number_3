import tkinter as tk 
from tkinter import ttk
from db.connection import get_connection
import services.crud_departments_service as sd

def table_departments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

class Departments():
    def __init__(self, inframe, table_frame):
        self.inframe = inframe
        self.table_frame = table_frame

    def del_widget(self, widget_to_keep):
        for widget in self.inframe.winfo_children():
            if widget != widget_to_keep: 
                widget.destroy()

    def refresh_table(self):
        # Xóa toàn bộ widget trong table_frame
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Tạo lại Treeview mới
        columns = ("Department ID", "Department Name")
        rows = table_departments()

        x_scrol = tk.Scrollbar(self.table_frame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(self.table_frame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        table = ttk.Treeview(
            self.table_frame,
            xscrollcommand=x_scrol.set,
            yscrollcommand=y_scrol.set,
            columns=columns,
            show="headings"
        )

        for col in columns:
            table.heading(col, text=col)
            table.column(col, anchor="center")

        for r in rows:
            table.insert("", "end", values=r)

        x_scrol.config(command=table.xview)
        y_scrol.config(command=table.yview)
        table.pack(side="left", fill="both", expand=True)

        return table

    def create(self):
        tk.Label(self.inframe, text= "Department Name",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)

        DepartmentName = tk.Entry(self.inframe, font=("Arial", 15))

        DepartmentName.place(x=150, y=200)

        tk.Button(self.inframe,command= lambda: (sd.create_department(DepartmentName.get()), 
                                                self.refresh_table()), text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11)).place(x=150, y= 276)

    def read(self):
        pass
    
    def update(self):
        tk.Label(self.inframe, text= "Department ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 136)
        tk.Label(self.inframe, text= "Department Name",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 226)

        DepartmentID = tk.Entry(self.inframe, font=("Arial", 15))
        DepartmentName = tk.Entry(self.inframe, font=("Arial", 15))


        DepartmentID.place(x=150, y=160)
        DepartmentName.place(x=150, y=250)

        button = tk.Button(self.inframe, command= lambda: (sd.update_department(DepartmentID.get(), DepartmentName.get()),
                                    self.refresh_table()),text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x= 150, y= 340)

    def delete(self):
        tk.Label(self.inframe, text= "Department ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)
        DepartmentID = tk.Entry(self.inframe, font=("Arial", 15))
        DepartmentID.place(x=150, y=200)

        button = tk.Button(self.inframe, command= lambda: (sd.delete_department(DepartmentID.get()),
                                                        self.refresh_table()),text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x=150, y= 280)