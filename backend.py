from database import get_connection

def add_expense(title, amount, category):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",(title, amount, category))

    conn.commit()
    conn.close()

def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()
    return data

def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

def clear_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses")
    conn.commit()
    conn.close()