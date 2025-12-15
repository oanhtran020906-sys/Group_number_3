from db.connection import get_connection
from decimal import Decimal
#Keyword chính là chức năng search nhé, nên bắt buộc phải truyền vào tham số
def search_and_filter(keyword, dept=None, proj=None, role=None, smin=None, smax=None, manager=None) :
    conn = get_connection()
    cursor = conn.cursor()   

    cursor.callproc("SearchAndFilter", [
        keyword,
        dept,
        proj,
        role,
        smin,
        smax,
        manager
    ])

    rows = []
    for result in cursor.stored_results():
        raw = result.fetchall()
        
        for row in raw:
            clean_row = [int(x) if isinstance(x, Decimal) and x == int(x)  #Đoạn này xử lý cái Decimal()
                     else float(x) if isinstance(x, Decimal) 
                     else x
                     for x in row]
            rows.append(clean_row)

    cursor.close()
    conn.close()
    return rows


       
