import sqlite3
from database import create_connection

def add_transaction(user_id, trans_type, category, amount, date):
    """Add an income or expense transaction."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (user_id, type, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, trans_type, category, amount, date))

    conn.commit()
    conn.close()

    print(f"{trans_type.capitalize()} added successfully!")

def delete_transaction(trans_id):
    """Delete a transaction by its ID."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE id = ?", (trans_id,))
    conn.commit()
    conn.close()

    print("Transaction deleted successfully!")





def set_budget(user_id, category, amount):
    """Set a budget for a category."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO budgets (user_id, category, amount)
        VALUES (?, ?, ?)
    ''', (user_id, category, amount))

    conn.commit()
    conn.close()

    print(f"Budget set for {category}!")

def check_budget(user_id, category):
    """Check if the user has exceeded the budget for a category."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND category = ? AND type = 'expense'
    ''', (user_id, category))
    total_expenses = cursor.fetchone()[0] or 0

    cursor.execute('''
        SELECT amount FROM budgets
        WHERE user_id = ? AND category = ?
    ''', (user_id, category))
    budget = cursor.fetchone()

    if budget and total_expenses > budget[0]:
        print(f"Warning: You have exceeded your budget for {category}!")
    else:
        print(f"You are within your budget for {category}.")
    
    conn.close()


