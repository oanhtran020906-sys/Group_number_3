import tkinter as tk
from tkinter import ttk, messagebox
from db.connection import get_connection
import bcrypt

class LoginWindow:
    def __init__(self, parent, on_login_success):
        self.parent = parent
        self.on_login_success = on_login_success
        self.window = tk.Toplevel(parent)
        self.window.title("Employee Information Manager - Login")
        self.window.geometry("400x500")
        self.window.configure(bg='#FFF0F5')  # Màu nền hồng pastel nhạt
        self.window.resizable(False, False)
        
        # Tạo style cho widget
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Cấu hình màu sắc
        self.configure_styles()
        
        # Tạo giao diện
        self.create_widgets()
        
        # Bind phím Enter để login
        self.window.bind('<Return>', lambda e: self.login())
        
    def configure_styles(self):
        """Cấu hình style cho các widget với theme hồng pastel"""
        # Màu chính
        bg_color = '#FFF0F5'      # Lavender blush
        fg_color = '#8B475D'      # Hồng đậm nhẹ
        btn_color = '#FFB6C1'     # Light pink
        entry_bg = '#FFFFFF'      # Trắng
        accent_color = '#FF69B4'  # Hot pink nhạt
        
        # Style cho Label
        self.style.configure('Pink.TLabel', 
                           background=bg_color,
                           foreground=fg_color,
                           font=('Segoe UI', 11))
        
        # Style cho Entry
        self.style.configure('Pink.TEntry',
                           fieldbackground=entry_bg,
                           foreground='#333333',
                           bordercolor=accent_color,
                           lightcolor=accent_color,
                           darkcolor=accent_color)
        
        # Style cho Button
        self.style.configure('Pink.TButton',
                           background=btn_color,
                           foreground=fg_color,
                           font=('Segoe UI', 10, 'bold'),
                           borderwidth=1,
                           focusthickness=3,
                           focuscolor='none')
        self.style.map('Pink.TButton',
                      background=[('active', '#FF82AB')],  # Màu khi hover
                      foreground=[('active', '#FFFFFF')])
    
    def create_widgets(self):
        """Tạo các widget cho giao diện đăng nhập"""
        # Container chính
        main_frame = tk.Frame(self.window, bg='#FFF0F5')
        main_frame.pack(fill='both', expand=True, padx=40, pady=30)
        
        # Tiêu đề
        title_label = tk.Label(
            main_frame,
            text=" EMPLOYEE INFORMATION MANAGER ",
            font=('Segoe UI', 18, 'bold'),
            fg='#FF69B4',
            bg='#FFF0F5'
        )
        title_label.pack(pady=(0, 30))
        
        # Phụ đề
        subtitle_label = tk.Label(
            main_frame,
            text="Welcome back! Please login to continue",
            font=('Segoe UI', 10),
            fg='#8B475D',
            bg='#FFF0F5'
        )
        subtitle_label.pack(pady=(0, 40))
        
        # Frame cho form
        form_frame = tk.Frame(main_frame, bg='#FFF0F5')
        form_frame.pack(fill='x', pady=10)
        
        # Username
        tk.Label(
            form_frame,
            text="Username:",
            font=('Segoe UI', 10, 'bold'),
            fg='#8B475D',
            bg='#FFF0F5'
        ).grid(row=0, column=0, sticky='w', pady=(0, 5))
        
        self.username_entry = ttk.Entry(
            form_frame,
            style='Pink.TEntry',
            font=('Segoe UI', 10),
            width=30
        )
        self.username_entry.grid(row=1, column=0, pady=(0, 20), ipady=8)
        self.username_entry.focus()  # Tự động focus vào username
        
        # Password
        tk.Label(
            form_frame,
            text="Password:",
            font=('Segoe UI', 10, 'bold'),
            fg='#8B475D',
            bg='#FFF0F5'
        ).grid(row=2, column=0, sticky='w', pady=(0, 5))
        
        self.password_entry = ttk.Entry(
            form_frame,
            style='Pink.TEntry',
            font=('Segoe UI', 10),
            show="•",
            width=30
        )
        self.password_entry.grid(row=3, column=0, pady=(0, 30), ipady=8)
        
        # Nút Login
        login_btn = ttk.Button(
            form_frame,
            text="LOGIN",
            style='Pink.TButton',
            command=self.login,
            width=20
        )
        login_btn.grid(row=4, column=0, pady=10, ipady=10)
        
        # Link "Forgot password?" (chỉ để trang trí)
        forgot_link = tk.Label(
            form_frame,
            text="Forgot password?",
            font=('Segoe UI', 9, 'underline'),
            fg='#FF69B4',
            bg='#FFF0F5',
            cursor="hand2"
        )
        forgot_link.grid(row=5, column=0, pady=(20, 0))
        forgot_link.bind('<Button-1>', lambda e: messagebox.showinfo("Info", "Contact administrator!"))
        
        # Decoration - các hình tròn trang trí
        self.create_decorations()
    
    def create_decorations(self):
        """Tạo các hình trang trí"""
        canvas = tk.Canvas(self.window, bg='#FFF0F5', highlightthickness=0, width=400, height=100)
        canvas.pack(side='bottom', fill='x')
        
        # Vẽ các hình tròn hồng
        colors = ['#FFB6C1', '#FFC0CB', '#FFD1DC', '#FFE4E1']
        positions = [(50, 20), (320, 40), (100, 70), (280, 15), (180, 50)]
        
        for pos, color in zip(positions, colors * 2):
            x, y = pos
            canvas.create_oval(x, y, x+40, y+40, fill=color, outline='')
    
    def login(self):
        """Xử lý đăng nhập"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Missing Information", 
                                 "Please enter both username and password!",
                                 parent=self.window)
            return
        
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT user_id, password_hash, employee_id FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if user and bcrypt.checkpw(password.encode(), user['password_hash'].encode()):
                # Hiệu ứng loading nhỏ
                self.show_loading_effect()
                
                # Đợi 1 chút rồi đóng
                self.window.after(500, lambda: self.finish_login(user))
            else:
                messagebox.showerror("Login Failed", 
                                   "Invalid username or password!",
                                   parent=self.window)
                # Hiệu ứng rung khi sai
                self.shake_window()
                
        except Exception as e:
            messagebox.showerror("Database Error", 
                               f"Could not connect to database:\n{str(e)}",
                               parent=self.window)
    
    def show_loading_effect(self):
        """Hiệu ứng loading nhỏ"""
        loading_label = tk.Label(
            self.window,
            text="Logging in...",
            font=('Segoe UI', 9),
            fg='#FF69B4',
            bg='#FFF0F5'
        )
        loading_label.place(relx=0.5, rely=0.9, anchor='center')
        self.window.update()
    
    def shake_window(self):
        """Hiệu ứng rung cửa sổ khi login sai"""
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        for _ in range(3):
            for dx, dy in [(10,0), (-10,0), (10,0), (-10,0), (0,0)]:
                self.window.geometry(f"+{x+dx}+{y+dy}")
                self.window.update_idletasks()
                self.window.after(50)
    
    def finish_login(self, user):
        """Hoàn thành login và gọi callback"""
        messagebox.showinfo("Welcome!", 
                          f"Login successful!\nWelcome, {self.username_entry.get()}!",
                          parent=self.window)
        self.window.destroy()
        self.on_login_success(user)
