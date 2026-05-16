from flask import Blueprint, request, jsonify
from app.services.db import get_db_connection

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/api/expenses', methods=['GET'])
def get_expenses():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM expenses ORDER BY created_at DESC")

    expenses = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(expenses)


@expenses_bp.route('/api/expenses', methods=['POST'])
def add_expense():

    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO expenses
        (title, amount, category, expense_date)
        VALUES (%s, %s, %s, %s)
        RETURNING *
    """

    cur.execute(query, (
        data['title'],
        data['amount'],
        data['category'],
        data['expense_date']
    ))

    new_expense = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    return jsonify(new_expense)