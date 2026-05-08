import sqlite3
import os

DB_PASSWORD = "supersecret123"
API_KEY = "sk-prod-abc123xyz789"


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Fetch user by username
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()


def run_report(report_name):
    os.system(f"./reports/{report_name}.sh")
trigger3
trigger4
