from db.connection import get_connection

#CREATE (CHECKED)
#Tạo bằng tên, ngày tháng năm sinh định dạng yyyy-mm-dd, và department ID
def create_employee(name, birth, department_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("CreateEmployee", [name, birth, department_id])
    conn.commit()
    cursor.close()
    conn.close()
    print ("Employee created successfully")

#READ ALL (CHECKED)
def get_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetEmployees")

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data
  

#READ BY ID (CHECKED)
def get_employee_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetEmployeeByID", [emp_id])

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data

#UPDATE (CHECKED)
#Tìm Employee ID để update
def update_employee(emp_id, name, birth, department_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("UpdateEmployee", [emp_id, name, birth, department_id])
    conn.commit()
    cursor.close()
    conn.close()
    print("Employee updated successfully")

#DELETE (CHECKED)
def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("DeleteEmployee", [emp_id])
    conn.commit()
    cursor.close()
    conn.close()
    print("Employee deleted successfully")

