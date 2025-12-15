import csv
from tkinter import filedialog, messagebox
from datetime import datetime
from tkinter import ttk
from main_window import Window

def get_treeview_in_frame(table_frame):
        for widget in table_frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                return widget
        return None

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
        