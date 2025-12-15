from db.connection import get_connection
import mysql.connector

#CREATE (CHECKED)
#Tạo bằng EmployeeID, Project ID, Role và Salary. Lỗi khi đã tồn tại cặp E-P trong bảng
def create_assignment(emp_id, project_id, role, salary):
    conn = get_connection()
    cursor = conn.cursor()

    try: 
        cursor.callproc("CreateAssignment", [emp_id, project_id, role, salary])
        conn.commit()
        print("Assignment created successfully")
    except mysql.connector.IntegrityError:
        print("This employee is already assigned to this project")
    finally :
        cursor.close()
        conn.close()

#READ ALL (CHECKED)
#Đọc toàn bộ
def get_assignments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetAssignments")

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data

#READ BY ID (CHECKED)
#Đọc bằng Assignment ID
def get_assignment_by_id(assign_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetAssignmentByID", [assign_id])

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data

#UPDATE (CHECKED)
#Tìm Assignment ID, có thể thay đổi E-P, Role và Salary
def update_assignment(aid, emp_id, project_id, role, salary):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("UpdateAssignment", [aid, emp_id, project_id, role, salary]) 
    conn.commit()
    cursor.close()
    conn.close()

#DELETE (CHECKED)
#Xóa bằng Assignment ID
def delete_assignment(aid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("DeleteAssignment", [aid])
    conn.commit()
    cursor.close()
    conn.close()
    print("Assignment deleted successfully")

