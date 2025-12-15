from db.connection import get_connection
import tkinter as tk
from tkinter import ttk


def select_dynamic_columns(columns):
    # columns là list các cột bạn muốn lấy
    cols = ", ".join(columns)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""SELECT {cols} FROM Employees e 
                    INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID
                    INNER JOIN Assignments a ON e.EmployeeID = a.EmployeeID
                    INNER JOIN Projects p ON a.ProjectID = p.ProjectID
                    ORDER BY e.EmployeeID, p.ProjectID;""")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows


class Queries_inner:
    def __init__(self, inframe, table_frame):
        self.inframe = inframe
        self.table_frame = table_frame

    def del_widget(self, widget_to_keep):
        for widget in self.inframe.winfo_children():
            if widget != widget_to_keep: 
                widget.destroy()

    def button_queries(self):
        tk.Label(self.inframe, text= "INNER JOIN", bg="#FFC0CB",fg="#7E7E7E", font=("Arial", 9)).place(x=350, y=15)

        tk.Label(self.inframe, text= "Projects", bg="#FFC0CB",fg="#535353", font=("Arial", 15)).place(x=100, y=320)
        tk.Label(self.inframe, text= "Assignments", bg="#FFC0CB",fg="#535353", font=("Arial", 15)).place(x=100, y=50)
        tk.Label(self.inframe, text= "Departments", bg="#FFC0CB",fg="#535353", font=("Arial", 15)).place(x=100, y=440)
        tk.Label(self.inframe, text= "Employees", bg="#FFC0CB",fg="#535353", font=("Arial", 15)).place(x=100, y=200)

        # Khai báo biến cho từng checkbox
        self.AssignmentID = tk.StringVar()
        #self.EmployeeID = tk.StringVar()
        #self.ProjectID = tk.StringVar()
        self.EmployeeRole = tk.StringVar()
        self.Salary = tk.StringVar()

        self.EmployeeID = tk.StringVar()
        self.EmployeeName = tk.StringVar()
        self.DateOfBirth = tk.StringVar()
        #self.DepartmentID = tk.StringVar()

        self.ProjectID = tk.StringVar()
        self.ProjectName = tk.StringVar()
        self.ManagerEmployeeID = tk.StringVar()

        self.DepartmentID = tk.StringVar()
        self.DepartmentName = tk.StringVar()

        tk.Checkbutton(self.inframe, text="Assignment ID", variable=self.AssignmentID,
                       onvalue="a.AssignmentID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=90)
        tk.Checkbutton(self.inframe, text="Employee ID", variable=self.EmployeeID,
                       onvalue="a.EmployeeID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=290, y=90)
        tk.Checkbutton(self.inframe, text="Project ID", variable=self.ProjectID,
                       onvalue="a.ProjectID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=120)
        tk.Checkbutton(self.inframe, text="Employee Role", variable=self.EmployeeRole,
                       onvalue="a.EmployeeRole", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=290, y=120)
        tk.Checkbutton(self.inframe, text="Salary", variable=self.Salary,
                       onvalue="a.Salary", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=150)

        tk.Checkbutton(self.inframe, text="Employee ID", variable=self.EmployeeID,
                       onvalue="e.EmployeeID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=240)
        tk.Checkbutton(self.inframe, text="Employee Name", variable=self.EmployeeName,
                       onvalue="e.EmployeeName", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=290, y=240)
        tk.Checkbutton(self.inframe, text="Date Of Birth", variable=self.DateOfBirth,
                       onvalue="e.DateOfBirth", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=270)
        tk.Checkbutton(self.inframe, text="Department ID", variable=self.DepartmentID,
                       onvalue="e.DepartmentID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=290, y=270)

        tk.Checkbutton(self.inframe, text="ProjectID", variable=self.ProjectID,
                       onvalue="p.ProjectID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=360)
        tk.Checkbutton(self.inframe, text="Project Name", variable=self.ProjectName,
                       onvalue="p.ProjectName", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=290, y=360)
        tk.Checkbutton(self.inframe, text="Manager Employee ID", variable=self.ManagerEmployeeID,
                       onvalue="p.ManagerEmployeeID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=390)

        tk.Checkbutton(self.inframe, text="Department ID", variable=self.DepartmentID,
                       onvalue="d.DepartmentID", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=110, y=480)
        tk.Checkbutton(self.inframe, text="Department Name", variable=self.DepartmentName,
                       onvalue="d.DepartmentName", offvalue="", bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=290, y=480)

        # Nút Check
        tk.Button(self.inframe, text="Check", width=24, height=2,
                  bg="#CA9292", font=("Arial", 12), command= lambda:  self.refresh_table()).place(x=150, y=540)

    def columns(self):
        selected = []
        for var in [ self.EmployeeID, self.EmployeeName, self.ProjectID, self.AssignmentID, self.EmployeeRole, self.Salary,self.DepartmentName,
                     self.DateOfBirth, self.ProjectName, self.ManagerEmployeeID, self.DepartmentID]:
            val = var.get()
            if val:  # nếu khác rỗng
                selected.append(val)

        rows = select_dynamic_columns(selected)

        cleaned = [col.split('.')[-1] for col in selected]

        return rows , tuple(cleaned)
    
    def refresh_table(self):
        # Xóa toàn bộ widget trong table_frame
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Tạo lại Treeview mới
        rows, columns = self.columns()

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




