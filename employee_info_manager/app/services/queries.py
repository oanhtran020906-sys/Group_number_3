from db.connection import get_connection
import mysql.connector
from mysql.connector import Error
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime

# ============ QUERY FUNCTIONS ============

def inner_join():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("InnerJoin")
    result = []
    for res in cursor.stored_results():
        result = res.fetchall()
    cursor.close()
    conn.close()
    return result

def left_join():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("LeftJoin")
    result = []
    for res in cursor.stored_results():
        result = res.fetchall()
    cursor.close()
    conn.close()
    return result

def multiple_join():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("MultiTableJoin")
    result = []
    for res in cursor.stored_results():
        result = res.fetchall()
    cursor.close()
    conn.close()
    return result


def above_global_average():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("AboveGlobalAverage")
    result = []
    for res in cursor.stored_results():
        result = res.fetchall()
    cursor.close()
    conn.close()
    return result

# ============ CSV EXPORT SERVICE ============

class CSVExportService:
    @staticmethod
    def export_from_treeview(treeview, query_name):
        """Export data from Treeview to CSV"""
        try:
            if not treeview.get_children():
                messagebox.showwarning("No Data", "No data to export!")
                return False
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                initialfile=f"{query_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            )
            
            if not filename:
                return False
            
            # Get column headers
            columns = treeview['columns']
            headers = []
            for col in columns:
                header_text = treeview.heading(col)['text']
                headers.append(header_text if header_text else col)
            
            # Get all data
            data = []
            for item in treeview.get_children():
                row_values = treeview.item(item, 'values')
                data.append(row_values)
            
            # Write to CSV
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                writer.writerows(data)
            
            messagebox.showinfo(
                "Export Successful",
                f"✓ {query_name} data exported successfully!\n\n"
                f"File: {filename}\n"
                f"Rows: {len(data)}\n"
                f"Columns: {len(headers)}"
            )
            return True
            
        except Exception as e:
            messagebox.showerror("Export Error", f"✗ Failed to export CSV:\n{str(e)}")
            return False

# ============ STYLED EXPORT BUTTON ============

class StyledExportButton(tk.Button):
    """Styled Export CSV button with icon-like appearance"""
    def __init__(self, parent, **kwargs):
        # Default styling based on screenshot
        defaults = {
            'text': ' 📥 Export CSV',
            'bg': '#4CAF50',  # Green background
            'fg': 'white',
            'font': ('Arial', 10, 'bold'),
            'bd': 0,
            'relief': 'raised',
            'padx': 15,
            'pady': 8,
            'cursor': 'hand2'
        }
        defaults.update(kwargs)
        super().__init__(parent, **defaults)
        
        # Bind hover effects
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def on_enter(self, e):
        self['bg'] = '#45a049'  # Darker green on hover
        self['relief'] = 'sunken'
        
    def on_leave(self, e):
        self['bg'] = '#4CAF50'  # Original green
        self['relief'] = 'raised'

# ============ MAIN APPLICATION ============

class QueryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Query System")
        self.root.geometry("1200x700")
        
        # Style configuration
        self.configure_styles()
        
        # Create Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each query
        self.create_inner_join_tab()
        self.create_left_join_tab()
        self.create_multi_join_tab()
        self.create_above_avg_tab()
    
    def configure_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        
        # Configure Tab style
        style.configure('Custom.TNotebook.Tab', 
                       padding=[20, 8], 
                       font=('Arial', 10, 'bold'))
        
        # Configure Treeview style
        style.configure("Treeview.Heading", 
                       font=('Arial', 10, 'bold'),
                       background='#f0f0f0',
                       relief='flat')
        
        style.configure("Treeview", 
                       font=('Arial', 9),
                       rowheight=25)
        
        self.notebook = ttk.Notebook(self.root, style='Custom.TNotebook')
    
    def create_query_tab(self, tab_name, query_title, query_type):
        """Create a standardized query tab"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=tab_name)
        
        # Header frame with title and export button
        header_frame = tk.Frame(frame, bg='white')
        header_frame.pack(fill='x', padx=15, pady=(15, 5))
        
        # Title
        title_label = tk.Label(header_frame, 
                              text=query_title,
                              font=('Arial', 16, 'bold'),
                              bg='white',
                              fg='#333333')
        title_label.pack(side='left')
        
        # Export CSV Button (Styled)
        export_btn = StyledExportButton(
            header_frame,
            command=lambda: self.export_query(query_type)
        )
        export_btn.pack(side='right', padx=10)
        
        # Separator
        separator = tk.Frame(frame, height=2, bg='#e0e0e0')
        separator.pack(fill='x', padx=15, pady=5)
        
        # Treeview container
        tree_container = tk.Frame(frame)
        tree_container.pack(fill='both', expand=True, padx=15, pady=10)
        
        # Create Treeview with scrollbars
        tree_frame = tk.Frame(tree_container)
        tree_frame.pack(fill='both', expand=True)
        
        # Vertical Scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.pack(side='right', fill='y')
        
        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        hsb.pack(side='bottom', fill='x')
        
        # Create Treeview
        tree = ttk.Treeview(tree_frame,
                           yscrollcommand=vsb.set,
                           xscrollcommand=hsb.set,
                           selectmode='extended',
                           show='headings')  # Hide first empty column
        
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        
        tree.pack(fill='both', expand=True)
        
        # Control frame
        control_frame = tk.Frame(frame, bg='white')
        control_frame.pack(fill='x', padx=15, pady=(5, 15))
        
        # Run Query Button
        run_btn = tk.Button(control_frame,
                           text=f"Run {tab_name} Query",
                           command=lambda: self.run_query(query_type, tree),
                           bg='#2196F3',  # Blue
                           fg='white',
                           font=('Arial', 10, 'bold'),
                           padx=20,
                           pady=8,
                           bd=0,
                           cursor='hand2')
        run_btn.pack(side='left')
        
        # Status label
        status_label = tk.Label(control_frame,
                               text="",
                               font=('Arial', 10),
                               bg='white',
                               fg='#666666')
        status_label.pack(side='left', padx=20)
        
        # Store references
        setattr(self, f"{query_type}_tree", tree)
        setattr(self, f"{query_type}_status", status_label)
        
        return frame
    
    def create_inner_join_tab(self):
        """Create tab for INNER JOIN query"""
        self.create_query_tab("INNER JOIN", 
                            "INNER JOIN Query Results", 
                            "inner_join")
    
    def create_left_join_tab(self):
        """Create tab for LEFT JOIN query"""
        self.create_query_tab("LEFT JOIN", 
                            "LEFT JOIN Query Results", 
                            "left_join")
    
    def create_multi_join_tab(self):
        """Create tab for MULTI JOIN query"""
        self.create_query_tab("MULTI JOIN", 
                            "MULTI TABLE JOIN Query Results", 
                            "multi_join")
    
    def create_above_avg_tab(self):
        """Create tab for ABOVE AVERAGE query"""
        self.create_query_tab("ABOVE AVG", 
                            "ABOVE GLOBAL AVERAGE Query Results", 
                            "above_avg")
    
    def run_query(self, query_type, treeview):
        """Run query and display results"""
        query_functions = {
            'inner_join': inner_join,
            'left_join': left_join,
            'multi_join': multiple_join,
            'above_avg': above_global_average
        }
        
        query_titles = {
            'inner_join': "INNER JOIN",
            'left_join': "LEFT JOIN",
            'multi_join': "MULTI TABLE JOIN",
            'above_avg': "ABOVE AVERAGE"
        }
        
        status_label = getattr(self, f"{query_type}_status")
        
        try:
            # Clear existing data
            for item in treeview.get_children():
                treeview.delete(item)
            
            # Clear existing columns
            treeview['columns'] = []
            
            # Get results
            results = query_functions[query_type]()
            
            if not results:
                status_label.config(text="No results found", fg="#FF9800")  # Orange
                return
            
            # Configure columns
            columns = list(results[0].keys())
            treeview['columns'] = columns
            
            # Format column headers
            for col in columns:
                header_text = col.replace('_', ' ').title()
                treeview.heading(col, text=header_text, anchor='w')
                treeview.column(col, width=180, anchor='w', stretch=True)
            
            # Insert data with alternating colors
            for i, row in enumerate(results):
                values = [str(row[col]) if row[col] is not None else "" for col in columns]
                treeview.insert('', 'end', values=values, tags=('evenrow' if i % 2 == 0 else 'oddrow',))
            
            # Configure tag colors for alternating rows
            treeview.tag_configure('evenrow', background='#f9f9f9')
            treeview.tag_configure('oddrow', background='white')
            
            status_label.config(
                text=f"✓ {query_titles[query_type]}: {len(results)} records loaded",
                fg="#4CAF50"  # Green
            )
            
        except Exception as e:
            status_label.config(
                text=f"✗ Error loading {query_titles[query_type]}: {str(e)[:50]}...",
                fg="#F44336"  # Red
            )
    
    def export_query(self, query_type):
        """Export query results to CSV"""
        query_map = {
            'inner_join': (getattr(self, 'inner_join_tree'), 'INNER_JOIN_Query'),
            'left_join': (getattr(self, 'left_join_tree'), 'LEFT_JOIN_Query'),
            'multi_join': (getattr(self, 'multi_join_tree'), 'MULTI_TABLE_JOIN_Query'),
            'above_avg': (getattr(self, 'above_avg_tree'), 'ABOVE_AVERAGE_Query')
        }
        
        if query_type in query_map:
            treeview, query_name = query_map[query_type]
            CSVExportService.export_from_treeview(treeview, query_name)

# ============ RUN APPLICATION ============

def run_queries():
    root = tk.Tk()
    app = QueryApp(root)
    root.mainloop()
