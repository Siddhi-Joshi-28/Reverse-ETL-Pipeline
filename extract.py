import psycopg2
import psycopg2.extras
from config import DB_CONFIG

def extract_customers():
    """Pull raw customer rows from the source PostgreSQL database."""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT * FROM customers;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    print(f"[EXTRACT] Pulled {len(rows)} rows from customers table")
    return [dict(row) for row in rows]

if __name__ == "__main__":
    data = extract_customers()
    for row in data:
        print(row)