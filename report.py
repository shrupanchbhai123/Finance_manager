from database import create_connection


def generate_report(user_id, period='monthly'):
    """Generate a financial report."""
    conn = create_connection()
    cursor = conn.cursor()

    if period == 'monthly':
        cursor.execute('''
            SELECT type, category, SUM(amount) FROM transactions
            WHERE user_id = ? AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
            GROUP BY type, category
        ''', (user_id,))
    else:  # yearly
        cursor.execute('''
            SELECT type, category, SUM(amount) FROM transactions
            WHERE user_id = ? AND strftime('%Y', date) = strftime('%Y', 'now')
            GROUP BY type, category
        ''', (user_id,))

    report_data = cursor.fetchall()

    print(f"{period.capitalize()} Financial Report")
    for row in report_data:
        print(f"Type: {row[0]}, Category: {row[1]}, Amount: {row[2]}")
    
    conn.close()
