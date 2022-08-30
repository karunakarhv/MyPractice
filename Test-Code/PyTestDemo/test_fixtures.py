"""
Arrange
    Pre Conditions
    Setup
Act
    Test
    Assert

    Test
    Assert

Cleanup
    Post Conditions
    Teardown
"""

import pytest

@pytest.fixture
def setup():
    print('Start Browser')
    yield
    print('close Browser')

def test_1(setup):
    print('Test 1')

def test_2(setup):
    print('Test 2')

def test_3(setup):
    print('Test 3')

def cleanup():
    print('requires cleanup')