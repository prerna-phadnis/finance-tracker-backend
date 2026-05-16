from app.db.connection import get_db_connection

def create_expense(data):

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO expenses
        (title, amount, category, user_id)

        VALUES (%s, %s, %s, %s)

        RETURNING id
    """

    values = (
        data["title"],
        data["amount"],
        data["category"],
        data["user_id"]
    )

    cursor.execute(query, values)

    expense_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return expense_id


def get_all_expenses():

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, amount, category
        FROM expenses
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    expenses = []

    for row in rows:
        expenses.append({
            "id": row[0],
            "title": row[1],
            "amount": float(row[2]),
            "category": row[3]
        })

    return expenses