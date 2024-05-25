from fastapi import FastAPI,Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        database="mydb",
        user="myuser",
        password="mypassword",
        host="localhost",
        port="5432"
    )
    return conn

app = FastAPI()

class User(BaseModel):
    name: str
    email : str
    phone :str

@app.get("/get-users")
def get_users(conn=Depends(get_connection)):
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)  # Verileri sözlük olarak döndürmek için
        cursor.execute("SELECT * FROM table1 where name='ali'")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return {"Hata": str(e)}
    finally:
        conn.close()


# @app.post("/add-user")
# def add_user(user: User, conn=Depends(get_connection)):
#     try:
#         cursor = conn.cursor()
#         insert_query = """
#         INSERT INTO table1 (name, email, phone) VALUES (%s, %s, %s) RETURNING id
#         """
#         cursor.execute(insert_query, (user.name, user.email, user.phone))
#         new_id = cursor.fetchone()[0]
#         conn.commit()
#         return {"id": new_id, "name": user.name, "email": user.email, "phone": user.phone}
#     except Exception as e:
#         conn.rollback()
#         raise HTTPException(status_code=400, detail=str(e))
#     finally:
#         conn.close()

@app.post("/users")
def create_user(user: User, conn=Depends(get_connection)):
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Telefon numarasının var olup olmadığını kontrol et
        cursor.execute("SELECT phone FROM table1 WHERE phone = %s", (user.phone,))
        row = cursor.fetchone()
        if row:
            return {"detail": "Böyle bir telefon numarası daha önce eklendi"}

        # Yeni kullanıcı ekleme
        cursor.execute("INSERT INTO table1 (name, email, phone) VALUES (%s, %s, %s)", (user.name, user.email, user.phone))
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


# Uygulamayı başlatmak için
# python -m uvicorn main:app --reload

"""
get -> select
post ->insert
pull -> update
delete -> delete
"""