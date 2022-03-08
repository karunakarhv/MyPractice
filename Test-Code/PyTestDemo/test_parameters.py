import pytest
import sys

@pytest.mark.parametrize('username, password', [
    ('karun', 'xyz'),
    ('adithi', 'xy'),
    ('Anshu', 'x'),
])

def test_login(username, password):
    print(username, password)