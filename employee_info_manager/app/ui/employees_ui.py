import tkinter as tk 
from tkinter import ttk
from db.connection import get_connection
import services.crud_employees_service as se

def table_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


class Employees():
    def __init__(self, inframe, table_frame):
        self.inframe = inframe
        self.table_frame = table_frame

    def del_widget(self, widget_to_keep):
        for widget in self.inframe.winfo_children():
            if widget != widget_to_keep: 
                widget.destroy()

    def refresh_table(self, data = None):
        # Xóa toàn bộ widget trong table_frame
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Tạo lại Treeview mới
        columns = ("Employee ID", "Employee Name", "Date Of Birth", "Department ID")
        if data == None:
            rows = table_employees()
        else: 
            rows = data

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
    
        tk.Label(self.inframe, text= "Employee Name",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 100)
        tk.Label(self.inframe, text= "Date Of Birth",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 200)
        tk.Label(self.inframe, text= "Department ID",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 300)

        EmployeeName = tk.Entry(self.inframe, font=("Arial", 15))
        DateOfBirth = tk.Entry(self.inframe, font=("Arial", 15))
        DepartmentID = tk.Entry(self.inframe, font=("Arial", 15))

        EmployeeName.place(x=150, y=124)
        DateOfBirth.place(x=150, y=224)
        DepartmentID.place(x=150, y=324)

        button = tk.Button(self.inframe, command= lambda: (se.create_employee(EmployeeName.get(), DateOfBirth.get(), DepartmentID.get()),
                                                           self.refresh_table()),text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11))
        button.place(x= 150, y= 410)

    def read(self):
        tk.Label(self.inframe, text= "Employee ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)

        EmployeeID = tk.Entry(self.inframe, font=("Arial", 15))

        EmployeeID.place(x=150, y=200)

        tk.Button(self.inframe,command= lambda: self.refresh_table(se.get_employee_by_id(EmployeeID.get())),
                                                 text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11)).place(x=150, y= 276)

    def update(self):
        tk.Label(self.inframe, text= "Employee ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 76)
        tk.Label(self.inframe, text= "Employee Name",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)
        tk.Label(self.inframe, text= "Date Of Birth",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 276)
        tk.Label(self.inframe, text= "Department ID",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 376)

        EmployeeID = tk.Entry(self.inframe, font=("Arial", 15))
        EmployeeName = tk.Entry(self.inframe, font=("Arial", 15))
        DateOfBirth = tk.Entry(self.inframe, font=("Arial", 15))
        Department = tk.Entry(self.inframe, font=("Arial", 15))

        EmployeeID.place(x=150, y=100)
        EmployeeName.place(x=150, y=200)
        DateOfBirth.place(x=150, y=300)
        Department.place(x=150, y=400)

        button = tk.Button(self.inframe, command= lambda: (se.update_employee(EmployeeID.get(), EmployeeName.get(), DateOfBirth.get(), Department.get()),
                                                        self.refresh_table()),text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11))
        button.place(x= 150, y= 480)

    def delete(self):
        tk.Label(self.inframe, text= "Employee ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)
        EmployeeID = tk.Entry(self.inframe, font=("Arial", 15))
        EmployeeID.place(x=150, y=200)

        button = tk.Button(self.inframe, command= lambda: (se.delete_employee(EmployeeID.get()),
                                        self.refresh_table()),text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x=150, y= 276)  