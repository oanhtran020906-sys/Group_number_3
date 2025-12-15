import tkinter as tk 
from tkinter import ttk
from db.connection import get_connection
import services.crud_assignments_service as sa

def table_assignments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


class Assignments():
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
        columns = ("Assignment ID","Employee ID", "Project ID", "Employee Role", "Salary")
        if data == None:
            rows = table_assignments()
        else: 
            rows = data

        x_scrol = tk.Scrollbar(self.table_frame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x" )

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
    
        tk.Label(self.inframe, text= "Employee ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 76)
        tk.Label(self.inframe, text= "Project ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)
        tk.Label(self.inframe, text= "Employee Role",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 276)
        tk.Label(self.inframe, text= "Salary",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 376)

        EmployeeID = tk.Entry(self.inframe, font=("Arial", 15))
        ProjectID = tk.Entry(self.inframe, font=("Arial", 15))
        EmployeeRole = tk.Entry(self.inframe, font=("Arial", 15))
        Salary = tk.Entry(self.inframe, font=("Arial", 15))

        EmployeeID.place(x=150, y=100)
        ProjectID.place(x=150, y=200)
        EmployeeRole.place(x=150, y=300)
        Salary.place(x=150, y=400)

        button = tk.Button(self.inframe, command= lambda: (sa.create_assignment(EmployeeID.get(), ProjectID.get(), EmployeeRole.get(), Salary.get()), 
                                                           self.refresh_table()),text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11))
        button.place(x= 150, y= 480)
    def read(self):
        tk.Label(self.inframe, text= "Assignment ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)

        AssignmentID = tk.Entry(self.inframe, font=("Arial", 15))
        AssignmentID.place(x=150, y=200)
        

        tk.Button(self.inframe, command=lambda: self.refresh_table(sa.get_assignment_by_id(AssignmentID.get()))
                                                , text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11)).place(x=150, y= 276)

    def update(self):
        tk.Label(self.inframe, text= "Assginment ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 46)
        tk.Label(self.inframe, text= "Employee ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 136)
        tk.Label(self.inframe, text= "Project ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 226)
        tk.Label(self.inframe, text= "Employee Role",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 316)
        tk.Label(self.inframe, text= "Salary",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 406)

        AssginmentID = tk.Entry(self.inframe, font=("Arial", 15))
        EmployeeID = tk.Entry(self.inframe, font=("Arial", 15))
        ProjectID = tk.Entry(self.inframe, font=("Arial", 15))
        EmployeeRole = tk.Entry(self.inframe, font=("Arial", 15))
        Salary = tk.Entry(self.inframe, font=("Arial", 15))

        AssginmentID.place(x=150, y=70)
        EmployeeID.place(x=150, y=160)
        ProjectID.place(x=150, y=250)
        EmployeeRole.place(x=150, y=340)
        Salary.place(x=150, y=430)

        button = tk.Button(self.inframe, command= lambda: (sa.update_assignment(AssginmentID.get(), EmployeeID.get(), ProjectID.get(), EmployeeRole.get(),Salary.get()),
                                                           self.refresh_table()) , text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x= 150, y= 500)

    def delete(self):
        tk.Label(self.inframe, text= "Assignments ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)
        AssignmentID = tk.Entry(self.inframe, font=("Arial", 15))
        AssignmentID.place(x=150, y=200)

        button = tk.Button(self.inframe, command= lambda: (sa.delete_assignment(AssignmentID.get()),
                self.refresh_table()), text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x=150, y= 276)       