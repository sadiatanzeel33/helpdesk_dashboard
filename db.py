import sqlite3
from datetime import datetime

DB_NAME = "helpdesk.db"

# Initialize the database and create the table if it does not exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            department TEXT NOT NULL,
            issue TEXT NOT NULL,
            created_at TEXT NOT NULL,
            status TEXT DEFAULT 'Open'
        )
    """)
    conn.commit()
    conn.close()

# Insert a new ticket
def insert_ticket(name, email, department, message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO tickets (name, email, department, issue, created_at, status)
        VALUES (?, ?, ?, ?, ?, 'Open')
    """, (name, email, department, issue, created_at))
    conn.commit()
    conn.close()

# Get all tickets
def get_all_tickets():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, department, issue, status FROM tickets")
    tickets = cursor.fetchall()
    conn.close()
    return tickets

# Resolve a ticket by ID
def resolve_ticket(ticket_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET status='Resolved' WHERE id=?", (ticket_id,))
    conn.commit()
    conn.close()

# Delete a ticket by ID
def delete_ticket(ticket_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id=?", (ticket_id,))
    conn.commit()
    conn.close()

from datetime import datetime

def insert_ticket(name, email, department, issue):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO tickets (name, email, department, issue, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, department, issue, created_at))
    conn.commit()
    conn.close()
