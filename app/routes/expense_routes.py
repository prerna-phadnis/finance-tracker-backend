from flask import Blueprint, request, jsonify

from app.repositories.expense_repository import (
    create_expense,
    get_all_expenses
)

expense_bp = Blueprint("expenses", __name__)

@expense_bp.route("/", methods=["GET"])
def fetch_expenses():

    expenses = get_all_expenses()

    return jsonify(expenses)


@expense_bp.route("/", methods=["POST"])
def add_expense():

    body = request.json

    expense_id = create_expense(body)

    return jsonify({
        "message": "Expense created",
        "expense_id": expense_id
    })