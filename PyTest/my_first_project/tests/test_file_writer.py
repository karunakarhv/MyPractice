import pytest
import os
from src.file_writer import write_to_file

def test_write_to_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    content = "Hello, World!"
    write_to_file(file_path, content)
    with open(file_path, 'r') as file:
        assert file.read() == content