import tkinter as tk 
from tkinter import ttk
from db.connection import get_connection
import services.crud_projects_service as sp

def table_projects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


class Projects():
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
        columns = ("Project ID", "Project Name", "Manager Employee ID")
        if data == None:
            rows = table_projects()
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
        tk.Label(self.inframe, text= "Project Name ",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 150)
        tk.Label(self.inframe, text= "Manager Employee ID",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 250)

        ProjectName = tk.Entry(self.inframe, font=("Arial", 15))
        ManagerEmployeeID = tk.Entry(self.inframe, font=("Arial", 15))

        ProjectName.place(x=150, y=174)
        ManagerEmployeeID.place(x=150, y=274)

        button = tk.Button(self.inframe, command= lambda:(sp.create_project(ProjectName.get(), ManagerEmployeeID.get()),
                                                          self.refresh_table()), text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11))
        button.place(x= 150, y= 370)

    def read(self):
        tk.Label(self.inframe, text= "Project ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)

        ProjectID = tk.Entry(self.inframe, font=("Arial", 15))

        ProjectID.place(x=150, y=200)

        tk.Button(self.inframe,command= lambda: self.refresh_table(sp.get_project_by_id(ProjectID.get()))
                                                , text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11)).place(x=150, y= 276)

    def update(self):
        tk.Label(self.inframe, text= "Project ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 100)
        tk.Label(self.inframe, text= "Project Name",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 200)
        tk.Label(self.inframe, text= "Manager Employee ID",bg="#FFC0CB", fg="#535353", font=("Arial", 11)).place(x=150, y= 300)

        ProjectID = tk.Entry(self.inframe, font=("Arial", 15))
        ProjectName = tk.Entry(self.inframe, font=("Arial", 15))
        ManagerEmployeeID = tk.Entry(self.inframe, font=("Arial", 15))

        ProjectID.place(x=150, y=124)
        ProjectName.place(x=150, y=224)
        ManagerEmployeeID.place(x=150, y=324)

        button = tk.Button(self.inframe, command= lambda: (sp.update_project(ProjectID.get(), ProjectName.get(), ManagerEmployeeID.get()),
                                        self.refresh_table()),text= "Enter", width= 24, height= 2,bg="#CA9292", font=("Arial", 11))
        button.place(x= 150, y= 410)

    def delete(self):
        tk.Label(self.inframe, text= "Project ID",bg="#FFC0CB",fg="#535353", font=("Arial", 11)).place(x=150, y= 176)
        ProjectID = tk.Entry(self.inframe, font=("Arial", 15))
        ProjectID.place(x=150, y=200)

        button = tk.Button(self.inframe, command= lambda: (sp.delete_project(ProjectID.get()),
                                        self.refresh_table()),text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x=150, y= 276)  