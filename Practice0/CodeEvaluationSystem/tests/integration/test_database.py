import sqlite3
import pytest
from infrastructure.database import save_code, get_code_by_lab
from domain.code import Code


@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")  # Используем in-memory БД для тестов
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE code (
        code_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        lab_number INTEGER,
        repo_url TEXT,
        content TEXT,
        status TEXT
    )
    """)
    conn.commit()
    yield conn
    conn.close()


def test_save_and_get_code(db_connection):
    sample_code = Code(None, 123, 1, "https://github.com/user/repo", "print('Hello')")

    save_code(sample_code, db_connection)  # Передаем тестовую БД

    codes = get_code_by_lab(1, db_connection)

    assert len(codes) == 1
    assert codes[0]["lab_number"] == 1
    assert codes[0]["repo_url"] == "https://github.com/user/repo"
