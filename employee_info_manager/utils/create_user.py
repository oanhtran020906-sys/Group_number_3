import bcrypt
from db.connection import get_connection

def create_user(username, plain_password, employee_id=None):
    """Tạo user mới với password đã hash"""
    # Hash password
    password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, employee_id) VALUES (%s, %s, %s)",
            (username, password_hash, employee_id)
        )
        conn.commit()
        print(f"✅ User '{username}' created successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Tạo user mẫu
if __name__ == "__main__":
    create_user("admin", "admin123", 1)
    create_user("root", "0328825202", 2)
    create_user("manager", "manager123", 3)
