import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

class EmployeeDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Dashboard - Database2")
        self.root.geometry("1400x800")
        
        # Define pink pastel color palette
        self.pastel_colors = {
            'background': '#fff5f7',      # Light pink background
            'card_bg': '#ffffff',         # White cards
            'primary': '#ffccd5',         # Light pink
            'secondary': '#ffb3c6',       # Pink
            'accent1': '#ff8fab',         # Medium pink
            'accent2': '#ff758f',         # Strong pink
            'accent3': '#ff4d6d',         # Dark pink
            'accent4': '#c9184a',         # Deep pink
            'text_dark': '#590d22',       # Dark rose text
            'text_light': '#800f2f',      # Medium rose text
            'success': '#b7e4c7',         # Pastel green
            'warning': '#ffe5d9',         # Pastel peach
            'info': '#caf0f8',            # Pastel blue
            'tab_active': '#ff4d6d',      # Strong pink for active tab
            'tab_inactive': '#ffb3c6',    # Light pink for inactive tab
            'border': '#ffccd5',          # Pink border
            'highlight': '#ff0a54'        # Bright pink for highlights
        }
        
        # Configure root background
        self.root.configure(bg=self.pastel_colors['background'])
        
        # Load data
        self.load_data()
        
        # Create Notebook (Tab container)
        self.create_notebook()
        
        # Create status bar
        self.create_status_bar()
        
    def load_data(self):
        """Load and preprocess data from database2.csv"""
        try:
            # Load the database2.csv file
            self.data = pd.read_csv('C:\\Users\\Hi\\Downloads\\Very important files\\DBMS\\Group_number_3\\employee_info_manager\\app\\services\\database.csv')
            print(f"Successfully loaded database2.csv")
            print(f"Total records: {len(self.data)}")
            
            # Calculate required metrics
            self.total_employees = self.data['EmployeeID'].nunique()
            self.total_departments = self.data['DepartmentName'].nunique()
            self.total_projects = self.data['ProjectName'].nunique()
            self.total_assignments = len(self.data)
            self.avg_salary = self.data['Salary'].mean()
            
            # Format salary as VND
            self.avg_salary_vnd = f"{self.avg_salary:,.0f} VND"
            
            # Calculate average salary per employee
            self.employee_avg_salary = self.data.groupby(['EmployeeID', 'EmployeeName'])['Salary'].mean().reset_index()
            self.employee_avg_salary.columns = ['EmployeeID', 'EmployeeName', 'AverageSalary']
            
            # Role distribution
            self.role_distribution = self.data['EmployeeRole'].value_counts().reset_index()
            self.role_distribution.columns = ['Role', 'Count']
            self.role_distribution['Percentage'] = (self.role_distribution['Count'] / len(self.data) * 100).round(2)
            
            # Department distribution
            self.dept_distribution = self.data['DepartmentName'].value_counts().reset_index()
            self.dept_distribution.columns = ['Department', 'Count']
            
            print(f"Data preprocessing completed!")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "File database2.csv not found!")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
            self.root.destroy()
    
    def create_notebook(self):
        """Create notebook with tabs for each requirement"""
        # Create Notebook widget with pink styling
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("Pink.TNotebook", 
                       background=self.pastel_colors['background'],
                       borderwidth=0)
        style.configure("Pink.TNotebook.Tab", 
                       font=('Arial', 11, 'bold'),
                       padding=[20, 10],
                       background=self.pastel_colors['tab_inactive'],
                       foreground=self.pastel_colors['text_dark'],
                       borderwidth=2,
                       relief=tk.RAISED)
        
        style.map("Pink.TNotebook.Tab",
                 background=[("selected", self.pastel_colors['tab_active']),
                           ("active", self.pastel_colors['accent2'])],
                 foreground=[("selected", "white"),
                           ("active", "white")])
        
        self.notebook = ttk.Notebook(self.root, style="Pink.TNotebook")
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Create different tabs
        self.create_overview_tab()
        
        self.create_salary_histogram_tab()
        self.create_top_employees_tab()
        self.create_role_distribution_tab()
    
    def create_overview_tab(self):
        """Create overview tab with all information"""
        tab1 = tk.Frame(self.notebook, bg=self.pastel_colors['background'])
        self.notebook.add(tab1, text="📋 Overview")
        
        # Title
        title_label = tk.Label(tab1, text="Employee Management Overview - Database2", 
                              font=('Arial', 24, 'bold'), 
                              bg=self.pastel_colors['background'],
                              fg=self.pastel_colors['accent4'])
        title_label.pack(pady=20)
        
        # Create main content frame
        content_frame = tk.Frame(tab1, bg=self.pastel_colors['background'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Left column: KPI Cards
        left_frame = tk.Frame(content_frame, bg=self.pastel_colors['background'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # KPI Cards Section
        kpi_section = tk.LabelFrame(left_frame, text="📊 Key Performance Indicators", 
                                   font=('Arial', 14, 'bold'), 
                                   bg=self.pastel_colors['background'],
                                   fg=self.pastel_colors['accent4'],
                                   relief=tk.FLAT, borderwidth=0)
        kpi_section.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.create_kpi_cards_overview(kpi_section)
        
        # Quick Statistics Section
        stats_section = tk.LabelFrame(left_frame, text="📈 Quick Statistics", 
                                     font=('Arial', 14, 'bold'), 
                                     bg=self.pastel_colors['background'],
                                     fg=self.pastel_colors['accent4'],
                                     relief=tk.FLAT, borderwidth=0)
        stats_section.pack(fill=tk.BOTH, expand=True)
        
        self.create_quick_stats(stats_section)
        
        # Right column: Salary Analysis and Database Info
        right_frame = tk.Frame(content_frame, bg=self.pastel_colors['background'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Salary Analysis Section
        salary_section = tk.LabelFrame(right_frame, text="💰 Salary Range Analysis", 
                                      font=('Arial', 14, 'bold'), 
                                      bg=self.pastel_colors['background'],
                                      fg=self.pastel_colors['accent4'],
                                      relief=tk.FLAT, borderwidth=0)
        salary_section.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.create_salary_analysis(salary_section)
        
        # Database Info Section
        info_section = tk.LabelFrame(right_frame, text="🗄️ Database Information", 
                                    font=('Arial', 14, 'bold'), 
                                    bg=self.pastel_colors['background'],
                                    fg=self.pastel_colors['accent4'],
                                    relief=tk.FLAT, borderwidth=0)
        info_section.pack(fill=tk.BOTH, expand=True)
        
        self.create_database_info(info_section)
    
    def create_kpi_cards_overview(self, parent):
        """Create KPI cards for overview tab"""
        kpi_frame = tk.Frame(parent, bg=self.pastel_colors['background'])
        kpi_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Define KPI data with pink pastel colors
        kpis = [
            ("👥 Total Employees", self.total_employees, 
             self.pastel_colors['primary'], self.pastel_colors['text_dark']),
            ("🏢 Departments", self.total_departments, 
             self.pastel_colors['secondary'], self.pastel_colors['text_dark']),
            ("📁 Unique Projects", self.total_projects, 
             self.pastel_colors['accent1'], self.pastel_colors['text_dark']),
            ("📋 Total Assignments", self.total_assignments, 
             self.pastel_colors['accent2'], self.pastel_colors['text_dark']),
            ("💰 Avg Salary", self.avg_salary_vnd, 
             self.pastel_colors['accent3'], "white")
        ]
        
        for i, (title, value, bg_color, fg_color) in enumerate(kpis):
            # Create card with rounded corners effect
            card = tk.Frame(kpi_frame, bg=bg_color, relief=tk.RAISED, 
                           borderwidth=0, highlightthickness=0)
            card.grid(row=0, column=i, padx=5, sticky='nsew', ipadx=20, ipady=30)
            
            # Make columns expand equally
            kpi_frame.grid_columnconfigure(i, weight=1)
            
            # Title
            title_label = tk.Label(card, text=title, bg=bg_color, 
                                  fg=fg_color,
                                  font=('Arial', 12, 'bold'))
            title_label.pack(pady=(10, 5))
            
            # Value
            value_label = tk.Label(card, text=str(value), bg=bg_color, 
                                  fg=fg_color,
                                  font=('Arial', 16, 'bold'))
            value_label.pack(pady=(5, 10))
            
            # Add subtle shadow effect
            card.config(highlightbackground=self.pastel_colors['border'], 
                       highlightthickness=1)
    
    def create_quick_stats(self, parent):
        """Create quick statistics section"""
        stats_frame = tk.Frame(parent, bg=self.pastel_colors['card_bg'])
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(stats_frame, text="Top Departments by Employee Count", 
                              font=('Arial', 12, 'bold'), 
                              bg=self.pastel_colors['card_bg'],
                              fg=self.pastel_colors['accent4'])
        title_label.pack(anchor='w', pady=(0, 10))
        
        # Style for treeview
        style = ttk.Style()
        style.configure("Pink.Treeview",
                       background=self.pastel_colors['card_bg'],
                       fieldbackground=self.pastel_colors['card_bg'],
                       foreground=self.pastel_colors['text_dark'],
                       rowheight=30)
        style.configure("Pink.Treeview.Heading",
                       font=('Arial', 10, 'bold'),
                       background=self.pastel_colors['primary'],
                       foreground=self.pastel_colors['text_dark'])
        
        tree = ttk.Treeview(stats_frame, columns=('Department', 'Employees'), 
                           show='headings', height=7, style="Pink.Treeview")
        tree.heading('Department', text='Department')
        tree.heading('Employees', text='Employees')
        tree.column('Department', width=200)
        tree.column('Employees', width=100, anchor='center')
        
        # Add department data with alternating colors
        for idx, row in self.dept_distribution.iterrows():
            tag = 'even' if idx % 2 == 0 else 'odd'
            tree.insert('', tk.END, values=(row['Department'], row['Count']), tags=(tag,))
        
        tree.tag_configure('even', background=self.pastel_colors['card_bg'])
        tree.tag_configure('odd', background=self.pastel_colors['primary'])
        
        tree.pack(fill=tk.BOTH, expand=True)
    
    def create_salary_analysis(self, parent):
        """Create salary analysis section"""
        stats_frame = tk.Frame(parent, bg=self.pastel_colors['card_bg'])
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Calculate salary statistics
        min_salary = self.data['Salary'].min()
        max_salary = self.data['Salary'].max()
        median_salary = self.data['Salary'].median()
        salary_std = self.data['Salary'].std()
        
        stats_text = f"""• Minimum Salary: {min_salary:,.0f} VND
• Maximum Salary: {max_salary:,.0f} VND
• Median Salary: {median_salary:,.0f} VND
• Average Salary: {self.avg_salary:,.0f} VND
• Salary Std Dev: {salary_std:,.0f} VND

• Salary Range: {max_salary - min_salary:,.0f} VND

• Assignments above average: {(self.data['Salary'] > self.avg_salary).sum():,}
• Assignments below average: {(self.data['Salary'] <= self.avg_salary).sum():,}"""
        
        stats_text_widget = tk.Text(stats_frame, height=12, font=('Arial', 11), 
                                   bg=self.pastel_colors['card_bg'],
                                   fg=self.pastel_colors['text_dark'],
                                   relief=tk.FLAT, borderwidth=0,
                                   wrap=tk.WORD)
        stats_text_widget.insert(tk.END, stats_text)
        stats_text_widget.config(state=tk.DISABLED)
        stats_text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_database_info(self, parent):
        """Create database information section"""
        info_frame = tk.Frame(parent, bg=self.pastel_colors['card_bg'])
        info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        info_text = f"""• Database contains {self.total_employees} unique employees
• Each employee has multiple project assignments ({self.total_assignments} total assignments)
• Average projects per employee: {self.total_assignments/self.total_employees:.1f}
• Database includes comprehensive role information across {self.total_departments} departments
• Each project has multiple team members with different roles
• Data shows real-world organizational structure with overlapping responsibilities"""
        
        info_text_widget = tk.Text(info_frame, height=8, font=('Arial', 11), 
                                  bg=self.pastel_colors['card_bg'],
                                  fg=self.pastel_colors['text_dark'],
                                  relief=tk.FLAT, borderwidth=0,
                                  wrap=tk.WORD)
        info_text_widget.insert(tk.END, info_text)
        info_text_widget.config(state=tk.DISABLED)
        info_text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
 
    def create_salary_histogram_tab(self):
        """Create tab for salary histogram"""
        tab3 = tk.Frame(self.notebook, bg=self.pastel_colors['background'])
        self.notebook.add(tab3, text="💰 Salary Distribution")
        
        # Title
        title_label = tk.Label(tab3, text="Salary Distribution Analysis", 
                              font=('Arial', 24, 'bold'), 
                              bg=self.pastel_colors['background'],
                              fg=self.pastel_colors['accent4'])
        title_label.pack(pady=20)
        
        # Create histogram
        self.create_salary_histogram_chart(tab3)
    
    def create_salary_histogram_chart(self, parent):
        """Create salary histogram with pink theme"""
        chart_frame = tk.Frame(parent, bg=self.pastel_colors['background'])
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        fig = Figure(figsize=(12, 6), dpi=80)
        fig.patch.set_facecolor(self.pastel_colors['card_bg'])
        ax = fig.add_subplot(111)
        ax.set_facecolor(self.pastel_colors['card_bg'])
        
        # Create histogram
        salaries = self.data['Salary'] / 1000000  # Convert to millions
        
        # Create bins with pink color gradient
        bins = np.linspace(salaries.min(), salaries.max(), 20)
        
        # Create custom pink gradient
        n, bins, patches = ax.hist(salaries, bins=bins, alpha=0.85, 
                                  color=self.pastel_colors['primary'], 
                                  edgecolor=self.pastel_colors['accent4'], 
                                  linewidth=1.5)
        
        # Add gradient effect to bars
        for i, patch in enumerate(patches):
            # Gradient from light pink to dark pink
            gradient = i / len(patches)
            red = 1.0 - (gradient * 0.3)
            green = 0.8 - (gradient * 0.4)
            blue = 0.9 - (gradient * 0.3)
            patch.set_facecolor((red, green, blue, 0.85))
        
        ax.set_xlabel('Salary (Millions VND)', fontsize=12, 
                     color=self.pastel_colors['text_dark'])
        ax.set_ylabel('Number of Assignments', fontsize=12, 
                     color=self.pastel_colors['text_dark'])
        ax.set_title('Employee Salary Distribution', fontsize=16, 
                    fontweight='bold', color=self.pastel_colors['accent4'])
        ax.grid(True, alpha=0.2, linestyle='--', color=self.pastel_colors['border'])
        
        # Add average line
        avg_salary = salaries.mean()
        ax.axvline(avg_salary, color=self.pastel_colors['accent4'], 
                  linestyle='--', linewidth=3, 
                  label=f'Average: {avg_salary:.1f}M VND')
        
        # Add median line
        median_salary = salaries.median()
        ax.axvline(median_salary, color=self.pastel_colors['accent3'], 
                  linestyle='-', linewidth=2, 
                  label=f'Median: {median_salary:.1f}M VND')
        
        ax.legend(facecolor=self.pastel_colors['card_bg'], 
                 edgecolor=self.pastel_colors['border'],
                 fontsize=10)
        
        # Format axis
        ax.tick_params(axis='x', rotation=45, colors=self.pastel_colors['text_dark'])
        ax.tick_params(axis='y', colors=self.pastel_colors['text_dark'])
        
        # Add count labels on top of bars
        for i, v in enumerate(n):
            if v > 0:
                ax.text(bins[i] + (bins[i+1]-bins[i])/2, v + 0.5, 
                       str(int(v)), ha='center', va='bottom', 
                       fontsize=9, color=self.pastel_colors['text_dark'],
                       bbox=dict(boxstyle='round', facecolor=self.pastel_colors['primary'], 
                                alpha=0.3, edgecolor='none'))
        
        # Set spines color
        for spine in ax.spines.values():
            spine.set_color(self.pastel_colors['border'])
        
        # Add statistics box
        stats_text = f"""Statistics:
        • Mean: {salaries.mean():.2f}M VND
        • Median: {salaries.median():.2f}M VND
        • Std Dev: {salaries.std():.2f}M VND
        • Min: {salaries.min():.2f}M VND
        • Max: {salaries.max():.2f}M VND"""
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
               fontsize=10, verticalalignment='top',
               bbox=dict(boxstyle='round', 
                        facecolor=self.pastel_colors['primary'],
                        alpha=0.3,
                        edgecolor=self.pastel_colors['border']),
               color=self.pastel_colors['text_dark'])
        
        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def create_top_employees_tab(self):
        """Create tab for top employees"""
        tab4 = tk.Frame(self.notebook, bg=self.pastel_colors['background'])
        self.notebook.add(tab4, text="👑 Top Employees")
        
        # Title
        title_label = tk.Label(tab4, text="Top Employees by Average Salary", 
                              font=('Arial', 24, 'bold'), 
                              bg=self.pastel_colors['background'],
                              fg=self.pastel_colors['accent4'])
        title_label.pack(pady=20)
        
        # Control frame for N selection
        control_frame = tk.Frame(tab4, bg=self.pastel_colors['background'])
        control_frame.pack(pady=10)
        
        tk.Label(control_frame, text="Show Top:", 
                font=('Arial', 11, 'bold'), 
                bg=self.pastel_colors['background'],
                fg=self.pastel_colors['text_dark']).pack(side=tk.LEFT, padx=5)
        
        self.top_n_var = tk.StringVar(value="15")
        top_n_options = ["10", "15", "20", "25", "30"]
        top_n_combo = ttk.Combobox(control_frame, textvariable=self.top_n_var, 
                                  values=top_n_options, state='readonly', 
                                  width=10, font=('Arial', 10))
        top_n_combo.pack(side=tk.LEFT, padx=5)
        
        update_btn = tk.Button(control_frame, text="Update", 
                              command=self.update_top_employees,
                              font=('Arial', 10), 
                              bg=self.pastel_colors['accent2'],
                              fg='white',
                              relief=tk.RAISED,
                              borderwidth=1)
        update_btn.pack(side=tk.LEFT, padx=10)
        
        # Create table
        self.create_top_employees_table(tab4)
    
    def create_top_employees_table(self, parent):
        """Create table for top employees"""
        table_frame = tk.Frame(parent, bg=self.pastel_colors['background'])
        table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 20))
        
        # Style for treeview
        style = ttk.Style()
        style.configure("EmployeePink.Treeview",
                       background=self.pastel_colors['card_bg'],
                       fieldbackground=self.pastel_colors['card_bg'],
                       foreground=self.pastel_colors['text_dark'],
                       rowheight=35)
        style.configure("EmployeePink.Treeview.Heading",
                       font=('Arial', 11, 'bold'),
                       background=self.pastel_colors['accent2'],
                       foreground='white')
        
        # Create Treeview
        columns = ('Rank', 'ID', 'Name', 'Department', 'Projects', 'Avg Salary (VND)')
        self.top_employees_tree = ttk.Treeview(table_frame, columns=columns, 
                                             show='headings', height=15, 
                                             style="EmployeePink.Treeview")
        
        # Define headings
        for col in columns:
            self.top_employees_tree.heading(col, text=col)
            self.top_employees_tree.column(col, width=100, anchor='center')
        
        self.top_employees_tree.column('Name', width=200, anchor='w')
        self.top_employees_tree.column('Department', width=150)
        self.top_employees_tree.column('Avg Salary (VND)', width=150)
        
        # Add scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.top_employees_tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.top_employees_tree.xview)
        self.top_employees_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Load initial data
        self.load_top_employees_table()
        
        # Grid layout
        self.top_employees_tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Tag configurations for alternating rows
        self.top_employees_tree.tag_configure('even', background=self.pastel_colors['card_bg'])
        self.top_employees_tree.tag_configure('odd', background=self.pastel_colors['primary'])
    
    def load_top_employees_table(self):
        """Load data into top employees table"""
        # Clear existing data
        for item in self.top_employees_tree.get_children():
            self.top_employees_tree.delete(item)
        
        # Get project count per employee
        project_counts = self.data.groupby('EmployeeID')['ProjectName'].nunique().reset_index()
        project_counts.columns = ['EmployeeID', 'Projects']
        
        # Get department for each employee
        employee_info = self.data[['EmployeeID', 'DepartmentName']].drop_duplicates()
        
        # Prepare data for display
        display_data = self.employee_avg_salary.copy()
        display_data = pd.merge(display_data, project_counts, on='EmployeeID', how='left')
        display_data = pd.merge(display_data, employee_info, on='EmployeeID', how='left')
        
        # Sort and get top N
        top_n = int(self.top_n_var.get())
        display_data = display_data.sort_values('AverageSalary', ascending=False).head(top_n)
        
        # Insert data with alternating pink colors
        for idx, row in display_data.iterrows():
            values = (
                idx + 1,
                row['EmployeeID'],
                row['EmployeeName'],
                row['DepartmentName'],
                row['Projects'],
                f"{row['AverageSalary']:,.0f}"
            )
            tag = 'even' if (idx + 1) % 2 == 0 else 'odd'
            self.top_employees_tree.insert('', tk.END, values=values, tags=(tag,))
    
    def update_top_employees(self):
        """Update top employees table based on selected N"""
        self.load_top_employees_table()
    
    def create_role_distribution_tab(self):
        """Create tab for role distribution"""
        tab5 = tk.Frame(self.notebook, bg=self.pastel_colors['background'])
        self.notebook.add(tab5, text="👥 Role Distribution")
        
        # Title
        title_label = tk.Label(tab5, text="Employee Role Distribution Analysis", 
                              font=('Arial', 24, 'bold'), 
                              bg=self.pastel_colors['background'],
                              fg=self.pastel_colors['accent4'])
        title_label.pack(pady=20)
        
        # Create two-column layout
        content_frame = tk.Frame(tab5, bg=self.pastel_colors['background'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left: Pie Chart
        left_frame = tk.LabelFrame(content_frame, text="📊 Role Distribution Pie Chart", 
                                  font=('Arial', 12, 'bold'), 
                                  bg=self.pastel_colors['background'],
                                  fg=self.pastel_colors['accent4'],
                                  relief=tk.FLAT, borderwidth=0)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.create_role_pie_chart(left_frame)
        
        # Right: Role Table
        right_frame = tk.LabelFrame(content_frame, text="📋 Role Statistics Table", 
                                   font=('Arial', 12, 'bold'), 
                                   bg=self.pastel_colors['background'],
                                   fg=self.pastel_colors['accent4'],
                                   relief=tk.FLAT, borderwidth=0)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        self.create_role_table(right_frame)
    
    def create_role_pie_chart(self, parent):
        """Create role distribution pie chart"""
        chart_frame = tk.Frame(parent, bg=self.pastel_colors['background'])
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        fig = Figure(figsize=(7, 6), dpi=80)
        fig.patch.set_facecolor(self.pastel_colors['card_bg'])
        ax = fig.add_subplot(111)
        ax.set_facecolor(self.pastel_colors['card_bg'])
        
        # Prepare data - get top 10 roles
        top_roles = self.role_distribution.head(10)
        roles = top_roles['Role']
        counts = top_roles['Count']
        percentages = top_roles['Percentage']
        
        # Create labels
        labels = [f'{role}' for role in roles]
        
        # Pink pastel colors for pie chart
        pink_palette = [
            '#ffccd5', '#ffb3c6', '#ff8fab', '#ff758f', '#ff4d6d',
            '#ff0a54', '#dc0a5e', '#c9184a', '#a4133c', '#800f2f'
        ]
        
        # Create pie chart
        explode = [0.05] * len(roles)
        wedges, texts, autotexts = ax.pie(counts, labels=labels, 
                                         colors=pink_palette[:len(roles)],
                                         explode=explode, autopct=lambda pct: f'{pct:.1f}%\n({int(pct/100*sum(counts))})', 
                                         startangle=90, textprops={'fontsize': 9})
        
        for text in texts:
            text.set_fontsize(9)
            text.set_fontweight('bold')
            text.set_color(self.pastel_colors['text_dark'])
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Top 10 Roles Distribution', fontsize=14, 
                    fontweight='bold', color=self.pastel_colors['accent4'])
        ax.axis('equal')
        
        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def create_role_table(self, parent):
        """Create role distribution table"""
        table_frame = tk.Frame(parent, bg=self.pastel_colors['background'])
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Style for treeview
        style = ttk.Style()
        style.configure("RolePink.Treeview",
                       background=self.pastel_colors['card_bg'],
                       fieldbackground=self.pastel_colors['card_bg'],
                       foreground=self.pastel_colors['text_dark'],
                       rowheight=30)
        style.configure("RolePink.Treeview.Heading",
                       font=('Arial', 10, 'bold'),
                       background=self.pastel_colors['accent1'],
                       foreground=self.pastel_colors['text_dark'])
        
        # Create Treeview
        columns = ('Role', 'Count', 'Percentage', 'Avg Salary (VND)')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                           height=15, style="RolePink.Treeview")
        
        # Define headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='center')
        
        tree.column('Role', width=180, anchor='w')
        
        # Add scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Calculate salary statistics per role
        role_stats = self.data.groupby('EmployeeRole')['Salary'].mean().round(0)
        
        # Insert data with alternating colors
        for idx, row in self.role_distribution.head(20).iterrows():
            avg_salary = role_stats.get(row['Role'], 0)
            
            # Alternate row colors
            tag = 'even' if idx % 2 == 0 else 'odd'
            tree.insert('', tk.END, values=(
                row['Role'],
                int(row['Count']),
                f"{row['Percentage']}%",
                f"{avg_salary:,.0f}" if avg_salary > 0 else 'N/A'
            ), tags=(tag,))
        
        # Configure tags for alternating colors
        tree.tag_configure('even', background=self.pastel_colors['card_bg'])
        tree.tag_configure('odd', background=self.pastel_colors['primary'])
        
        # Grid layout
        tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
    
    def create_status_bar(self):
        """Create status bar"""
        status_frame = tk.Frame(self.root, bg=self.pastel_colors['accent4'], height=30)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Data info
        data_info = f"Database: database2.csv | Total Records: {len(self.data):,} | Unique Employees: {self.total_employees} | Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        status_label = tk.Label(status_frame, text=data_info, 
                               bg=self.pastel_colors['accent4'], 
                               fg='white', 
                               font=('Arial', 9))
        status_label.pack(side=tk.LEFT, padx=10)
        
        # Add refresh button
        refresh_btn = tk.Button(status_frame, text="🔄 Refresh Dashboard", 
                               command=self.refresh_data,
                               font=('Arial', 9), 
                               bg=self.pastel_colors['accent3'],
                               fg='white',
                               relief=tk.FLAT)
        refresh_btn.pack(side=tk.RIGHT, padx=10, pady=2)
    
    def refresh_data(self):
        """Refresh all data and reload the dashboard"""
        try:
            # Reload data from file
            self.data = pd.read_csv('database2.csv')
            
            # Recalculate metrics
            self.total_employees = self.data['EmployeeID'].nunique()
            self.total_departments = self.data['DepartmentName'].nunique()
            self.total_projects = self.data['ProjectName'].nunique()
            self.total_assignments = len(self.data)
            self.avg_salary = self.data['Salary'].mean()
            self.avg_salary_vnd = f"{self.avg_salary:,.0f} VND"
            
            # Recalculate employee average salary
            self.employee_avg_salary = self.data.groupby(['EmployeeID', 'EmployeeName'])['Salary'].mean().reset_index()
            self.employee_avg_salary.columns = ['EmployeeID', 'EmployeeName', 'AverageSalary']
            
            # Recalculate role distribution
            self.role_distribution = self.data['EmployeeRole'].value_counts().reset_index()
            self.role_distribution.columns = ['Role', 'Count']
            self.role_distribution['Percentage'] = (self.role_distribution['Count'] / len(self.data) * 100).round(2)
            
            # Recalculate department distribution
            self.dept_distribution = self.data['DepartmentName'].value_counts().reset_index()
            self.dept_distribution.columns = ['Department', 'Count']
            
            # Destroy all widgets and recreate
            for widget in self.root.winfo_children():
                widget.destroy()
            
            # Recreate the notebook and status bar
            self.create_notebook()
            self.create_status_bar()
            
            messagebox.showinfo("Refresh Successful", "Dashboard data has been refreshed!")
            
        except Exception as e:
            messagebox.showerror("Refresh Error", f"Failed to refresh data: {str(e)}")

def main():
    root = tk.Tk()
    
    # Set window properties
    root.title("Employee Dashboard - Database2")
    root.geometry("1400x800")
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    app = EmployeeDashboard(root)
    
    # Bind escape key to close
    root.bind('<Escape>', lambda e: root.quit())
    
    root.mainloop()

if __name__ == "__main__":
    main()
