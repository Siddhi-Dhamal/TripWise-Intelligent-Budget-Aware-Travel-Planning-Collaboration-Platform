import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    database_url = os.environ["DATABASE_URL"]
    try:
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"database_connected": True, "result": result}
    except Exception as e:
        return {"database_connected": False, "error": str(e)}