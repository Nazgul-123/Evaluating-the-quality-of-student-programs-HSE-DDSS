import sqlite3

conn = sqlite3.connect("dss.db")

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        username TEXT,
        role TEXT CHECK(role IN ('student', 'teacher', 'admin')),
        group_name TEXT,
        github_username TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS code (
        code_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        lab_number INTEGER,
        repo_url TEXT,
        content TEXT,
        status TEXT CHECK(status IN ('pending', 'checked')),
        FOREIGN KEY (student_id) REFERENCES users (user_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        report_id INTEGER PRIMARY KEY AUTOINCREMENT,
        code_id INTEGER,
        score INTEGER,
        feedback TEXT,
        FOREIGN KEY (code_id) REFERENCES code (code_id)
    )
    """)

    conn.commit()


def save_code(code):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO code (student_id, lab_number, repo_url, content, status) VALUES (?, ?, ?, ?, ?)",
                   (code.student_id, code.lab_number, code.repo_url, code.content, code.status))
    conn.commit()
