import pytest
from src.database import Database

@pytest.fixture
def database():
    db = Database()
    db.add("name", "Alice")
    db.add("age", 30)
    return db

def test_database_add(database):
    assert database.get("name") == "Alice"
    assert database.get("age") == 30

def test_database_get_nonexistent_key(database):
    assert database.get("address") is None