import pytest
from src.greeting import greet

def test_greet_morning(monkeypatch):
    class MockDateTime:
        @staticmethod
        def now():
            class MockDateTime:
                hour = 10
            return MockDateTime()

    monkeypatch.setattr("datetime.datetime", MockDateTime)
    assert greet() == "Good morning!"

def test_greet_afternoon(monkeypatch):
    class MockDateTime:
        @staticmethod
        def now():
            class MockDateTime:
                hour = 15
            return MockDateTime()

    monkeypatch.setattr("datetime.datetime", MockDateTime)
    assert greet() == "Good afternoon!"

def test_greet_evening(monkeypatch):
    class MockDateTime:
        @staticmethod
        def now():
            class MockDateTime:
                hour = 20
            return MockDateTime()

    monkeypatch.setattr("datetime.datetime", MockDateTime)
    assert greet() == "Good evening!"