from db.connection import get_connection
import tkinter as tk
from tkinter import ttk
from services.search_filter import search_and_filter
 
class search_filter(): 
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
        columns = ("Employee ID", "Employee Name", "Department Name", "Project Name", "Role", "Salary")
        result = search_and_filter(
    self.key.get() if self.key.get().strip() != "" else None,
    self.department.get() if self.department.get().strip() != "" else None,
    self.project.get() if self.project.get().strip() != "" else None,
    self.role.get() if self.role.get().strip() != "" else None,
    self.salary_min.get() if self.salary_min.get().strip() != "" else None,
    self.salary_max.get() if self.salary_max.get().strip() != "" else None
)

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

        for r in result:
            table.insert("", "end", values=r)

        x_scrol.config(command=table.xview)
        y_scrol.config(command=table.yview)
        table.pack(side="left", fill="both", expand=True)

        return table   
    
    def view(self):
        tk.Label(self.inframe, text= "Employee Name",  bg="#FFC0CB",fg="#535353", font= ("Arial")).place(x=100, y= 80)
        tk.Label(self.inframe, text= "Department", bg="#FFC0CB",fg="#535353",font= ("Arial")).place(x=130, y= 160)
        tk.Label(self.inframe, text= "Project", bg="#FFC0CB",fg="#535353",font= ("Arial")).place(x=160, y= 240)
        tk.Label(self.inframe, text= "Role", bg="#FFC0CB",fg="#535353",font= ("Arial")).place(x=180, y= 320)
        tk.Label(self.inframe, text= "Salary from", bg="#FFC0CB",fg="#535353",font= ("Arial")).place(x=100, y= 400)
        tk.Label(self.inframe, text= "to", bg="#FFC0CB",fg="#535353",font= ("Arial")).place(x=300, y= 400)

        self.key = tk.Entry(self.inframe, font=("Arial",10))
        self.department = ttk.Combobox(self.inframe, values=['Data Science','Engineering','Finance', 'Human Resources', 'Legal Affairs', 'Marketing', 'Sales'], state= "normal", font=("Arial", 10))
        self.project = ttk.Combobox(self.inframe, values=[
    'Economic Policy Research 2024',
    'MBA Program Improvement',
    'Financial Market Analysis',
    'Audit Process Optimization',
    'Urban Development Research',
    'Academic Administration Management',
    'Recruitment and HR Improvement',
    'Learning Management Software',
    'Data Analytics Platform',
    'AI Research Initiative',
    'Customer Segmentation Model',
    'Predictive Maintenance System',
    'Product Design Revamp',
    'Quality Assurance Framework',
    'Employee Engagement Program',
    'Talent Development Plan',
    'Legal Compliance Audit',
    'Contract Management System',
    'Market Expansion Strategy',
    'Brand Awareness Campaign',
    'Sales Optimization Program',
    'Customer Relationship Management',
    'Financial Reporting System',
    'Risk Management Framework',
    'HR Digital Transformation',
    'Performance Management System',
    'Legal Tech Implementation',
    'Corporate Governance Project',
    'Digital Marketing Campaign',
    'E-commerce Platform',
    'Supply Chain Optimization',
    'Logistics Management',
    'Cloud Migration Project',
    'Cybersecurity Initiative',
    'Mobile App Development',
    'Web Platform Redesign',
    'Big Data Infrastructure',
    'Machine Learning Models',
    'IoT Implementation',
    'Smart Factory Project'
]
, state= "normal", font=("Arial", 10))

        self.role = tk.Entry(self.inframe, font= ("Arial",10) )
        self.salary_min = tk.Entry(self.inframe, width=13, font= ("Arial",10))
        self.salary_max = tk.Entry(self.inframe, width=13, font= ("Arial",10))

        self.key.place(x = 240, y = 80)
        self.department.place(x= 240, y= 160)
        self.project.place(x=240, y=240)
        self.role.place(x=240, y=320)
        self.salary_min.place(x= 195, y= 400)
        self.salary_max.place(x= 330, y= 400)

        button = tk.Button(self.inframe, command= self.refresh_table,text= "Enter", width= 24, height= 2, bg= "#CA9292" ,font=("Arial", 12))
        button.place(x= 150, y= 500)




        