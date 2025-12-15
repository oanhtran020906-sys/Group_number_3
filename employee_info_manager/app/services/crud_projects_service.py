from db.connection import get_connection

#CREATE (CHECKED)
def create_project(name, manager_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("CreateProject", [name, manager_id])
    conn.commit()
    cursor.close()
    conn.close()
    print("Project created successfully")

#READ ALL (CHECKED)
def get_projects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetProjects")

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data

#READ BY ID (CHECKED)
def get_project_by_id(pid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("GetProjectByID", [pid])

    data = []
    for result in cursor.stored_results():
        data = result.fetchall()

    cursor.close()
    conn.close()
    return data

#UPDATE (CHECKED)
def update_project(pid, name, manager_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("UpdateProject", [pid, name, manager_id])
    conn.commit()
    cursor.close()
    conn.close()
    print("Project updated successfully")

#DELETE (CHECKED) 
def delete_project(pid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("DeleteProject", [pid])
    conn.commit()
    cursor.close()
    conn.close()
    print("Project deleted successfully")

