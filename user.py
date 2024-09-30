import sqlite3
from database import create_connection

def register(username, password):
    """Register a new user."""
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        conn.close()

def login(username, password):
    """Authenticate a user."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        print("Login successful!")
        return user[0]  # Return user_id
    else:
        print("Invalid credentials!")
        return None
