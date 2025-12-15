from db.connection import get_connection

# CREATE (CHECKED)
#Tạo bằng tên để nó tự gen ra ID
def create_department(name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc("CreateDepartments", [name])
        conn.commit() 

        rows = []
        for result in cursor.stored_results():
            rows = result.fetchall()

        return rows
    finally:
        cursor.close()
        conn.close()


# READ ALL (CHECKED)
#Đọc tất cả Department
def get_department():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetDepartments")

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data

# UPDATE (CHECKED)
#Update bằng tìm Department ID và đổi tên
def update_department(dept_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("UpdateDepartment", [dept_id, name])
    conn.commit()
    cursor.close()
    conn.close()

# DELETE (CHECKED)
#Xóa bằng Department ID
def delete_department(dept_id): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("DeleteDepartment", [dept_id])
    conn.commit()
    cursor.close()
    conn.close()

