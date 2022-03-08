import pytest
import sys

@pytest.mark.smoke
def test_login():
    print('Login Done')

@pytest.mark.xfail
def test_addProduct():
    assert False
    print('Added Product')

@pytest.mark.skipif(sys.version_info<(3, 9), reason='python version not supported')
def test_logout():
    print('Logout Done')