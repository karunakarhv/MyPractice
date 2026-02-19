import pytest
from src.person import Person

def test_person_introduction():
    person = Person("Alice", 30)
    assert person.introduce() == "Hi, I'm Alice and I'm 30 years old."

def test_person_attributes():
    person = Person("Bob", 25)
    assert person.name == "Bob"
    assert person.age == 25