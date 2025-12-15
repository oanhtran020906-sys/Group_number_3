import tkinter as tk 
from tkinter import ttk
import services.dashboard as db
from ui.assignments_ui import table_assignments, Assignments
from ui.departments_ui import table_departments, Departments
from ui.employees_ui import table_employees, Employees
from ui.projects_ui import table_projects, Projects
import ui.queries__inner as qi
from services.queries import run_queries
import ui.seach_and_filter as sf



def Window(root):
    title = tk.Label(root, text= "Employee Information Manager", bg="#A3D0E2" ,font=("Arial", 20, "bold"))
    title.pack(fill= "x", side="top")
    width = root.winfo_screenwidth()

    #Frame shows input 
    inframe = tk.Frame(root, bg="#FFC0CB",width= width/3)
    inframe.pack(fill="y",side="left")
    inframe.grid_propagate(False)

    inframe.grid_rowconfigure(0, weight=1)
    inframe.grid_columnconfigure(0, weight=1)


    #frame shows button, place in inframe
    buttoninframe = tk.Frame(inframe, bg="#FFC0CB")
    buttoninframe.grid(row=0, column=0, sticky="wsn")

    for i in range(8):  # có 8 hàng từ 0 đến 7
        buttoninframe.grid_rowconfigure(i, weight=1)
    
    def show_queries_inner():
        query_inner.del_widget(buttoninframe)
        query_inner.button_queries()

    def show_sefi():
        sefi.del_widget(buttoninframe)
        sefi.view()

    create = tk.Button(buttoninframe, text= "Create", width=8, height=4, font=("Arial", 10), bg="#FF69B4", fg="white" )
    read = tk.Button(buttoninframe,  text= "Read", width=8, height=4, font=("Arial", 10), bg="#FF69B4", fg="white")
    update = tk.Button(buttoninframe,  text= "Update", width=8, height=4, font=("Arial", 10), bg="#FF69B4", fg="white")
    delete = tk.Button(buttoninframe, text= "Delete", width=8, height=4, font=("Arial", 10), bg="#FF69B4", fg="white")
    queries_inner = tk.Button(buttoninframe, command= show_queries_inner, text= """Global
Columns""", width=8, height=5, font=("Arial", 10), bg="#FF69B4", fg="white")
    queries = tk.Button(buttoninframe, command= run_queries ,text= "Queries", width=8, height=4, font=("Arial", 10), bg="#FF69B4", fg="white")
    search_filtr = tk.Button(buttoninframe, text= """Search
and 
Filter""", command= show_sefi ,width=8, height=5, font=("Arial", 10), bg="#FF69B4", fg="white")
    dashboard = tk.Button(buttoninframe, command=db.main, text= "Dashboard", width=8, height=4, font=("Arial", 10), bg="#FF69B4", fg="white")
    create.grid(row=0, column=0, sticky="sn")
    read.grid(row=1, column=0, sticky="sn")
    update.grid(row=2, column=0, sticky="sn")
    delete.grid(row=3, column=0, sticky="sn")
    queries_inner.grid(row=4, column=0, sticky="sn")
    queries.grid(row=6, column=0, sticky="sn")
    search_filtr.grid(row=5, column=0, sticky="sn")
    dashboard.grid(row=7, column=0, sticky="sn")


    #Frame shows output 
    
    outframe = tk.Frame(root, bg= "#F7E9E9")
    outframe.pack(fill= "both", side="right", expand= True)
    outframe.pack_propagate(False)

    outframe.grid_rowconfigure(0, weight=0)
    outframe.grid_rowconfigure(1, weight=1)
    outframe.grid_columnconfigure(0, weight=1)


    #frame shows button, place in outframe
    button_frame = tk.Frame(outframe, bg="#F7E9E9")
    button_frame.grid(row=0, column=0, sticky="ew")

    for i in range(4):  # có 4 nút
        button_frame.grid_columnconfigure(i, weight=1)

    assignments = tk.Button(button_frame, command= lambda: show_table("assignments"), text= "Assignments",width=35, height=1, font=("Arial", 10), bg="#F5B2B2", fg="white")
    departments = tk.Button(button_frame, command= lambda: show_table("departments"), text="Departments",width=35, height=1, font=("Arial", 10), bg="#F5B2B2", fg="white")
    employees = tk.Button(button_frame, command= lambda: show_table("employees"), text="Employees",width=35, height=1, font=("Arial", 10), bg="#F5B2B2", fg="white")
    projects = tk.Button(button_frame, command= lambda: show_table("projects"), text= "Projects",width=35, height=1, font=("Arial", 10), bg="#F5B2B2", fg="white")
    assignments.grid(row=0, column=0)
    departments.grid(row=0,column=1)
    employees.grid(row=0, column=2)
    projects.grid(row=0, column=3)
    
    #Frame show table, place in outframe
    table_frame = tk.Frame(outframe, bg= "#F7E9E9")
    table_frame.grid(row=1, column=0, sticky="nsew")

    def show_table(name_table):
        for widget in table_frame.winfo_children():
            widget.destroy()

        if name_table == "assignments":
            columns = ("Assignment ID","Employee ID", "Project ID", "Employee Role", "Salary")
            rows = table_assignments()
            class_table("assignments")
        elif name_table == "departments":
            columns = ("Department ID", "Department Name")
            rows = table_departments()
            class_table("departments")
        elif name_table == "employees":
            columns = ("Employee ID", "Employee Name", "Date Of Birth", "Department ID")
            rows = table_employees()
            class_table("employees")
        elif name_table == "projects":
            columns = ("Project ID", "Project Name", "Manager Employee ID")
            rows = table_projects()
            class_table("projects")

        x_scrol = tk.Scrollbar(table_frame, orient= "horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(table_frame, orient= "vertical")
        y_scrol.pack(side="right", fill="y")
        
        table = ttk.Treeview(table_frame, xscrollcommand= x_scrol.set, yscrollcommand= y_scrol.set, columns= columns, show= "headings")
        
        for row in columns:
            table.heading(row, text= row)
            table.column(row, anchor= "center")
        for i in rows:
            table.insert("", "end", values= i)
        
        x_scrol.config(command=table.xview)
        y_scrol.config(command=table.yview)
        table.pack(side="left", fill= "both", expand= True)

    def class_table(name):
        if name == "assignments":
            name = Assignments(inframe, table_frame)
        elif name == "departments":
            name = Departments(inframe, table_frame)
        elif name == "employees":
            name = Employees(inframe, table_frame)
        elif name == "projects":
            name = Projects(inframe, table_frame)
        
        create.config(command= lambda: (name.del_widget(buttoninframe), name.create()))
        read.config(command= lambda: (name.del_widget(buttoninframe), name.read()))
        update.config(command= lambda: (name.del_widget(buttoninframe), name.update()))
        delete.config(command= lambda: (name.del_widget(buttoninframe), name.delete()))

    #Button queries
    query_inner = qi.Queries_inner(inframe, table_frame)
    sefi = sf.search_filter(inframe, table_frame)
