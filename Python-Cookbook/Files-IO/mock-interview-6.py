# Practice Pytest
# Task: Write a pytest function to test the extract_log_fields function from the previous exercise.
import re
import pytest
def extract_log_fields(log_line):
    pattern = r'\[(.*?)\] ID:(\d+) \| STATUS:(\w+) \| LATENCY:(\d+ms) \| CODEC:(\w+)'
    if log_line is None:
        return None
    match = re.search(pattern, log_line)
    if match:
        timestamp = match.group(1)
        session_id = match.group(2)
        status = match.group(3)
        latency = match.group(4)
        codec = match.group(5)
        return {
            'timestamp': timestamp,
            'session_id': session_id,
            'status': status,
            'latency': latency,
            'codec': codec
        }
    else:
        return None
    
# write a pytest function to test the extract_log_fields function
def test_extract_log_fields():
    log_line = "[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms | CODEC:AC4"
    expected_output = {
        'timestamp': '2026-02-07 10:15:01',
        'session_id': '9922',
        'status': 'OK',
        'latency': '120ms',
        'codec': 'AC4'
    }
    assert extract_log_fields(log_line) == expected_output

# add some edge cases
def test_extract_log_fields_edge_cases():
    # Test with missing fields
    log_line_missing_fields = "[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms"
    assert extract_log_fields(log_line_missing_fields) is None
    
    # Test with extra fields
    log_line_extra_fields = "[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms | CODEC:AC4 | EXTRA:VALUE"
    expected_output_extra = {
        'timestamp': '2026-02-07 10:15:01',
        'session_id': '9922',
        'status': 'OK',
        'latency': '120ms',
        'codec': 'AC4'
    }
    assert extract_log_fields(log_line_extra_fields) == expected_output_extra
    
# Add parametrized test cases
@pytest.mark.parametrize("log_line, expected_output", [
    ("[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms | CODEC:AC4", {
        'timestamp': '2026-02-07 10:15:01',
        'session_id': '9922',
        'status': 'OK',
        'latency': '120ms',
        'codec': 'AC4'
    }),
    ("[2026-02-07 10:15:05] ID:9923 | STATUS:FAIL | ERR:Buffer_Underrun | LATENCY:450ms", None),
    ("[2026-02-07 10:15:10] ID:9924 | STATUS:OK | LATENCY:110ms | CODEC:AC4", {
        'timestamp': '2026-02-07 10:15:10',
        'session_id': '9924',
        'status': 'OK',
        'latency': '110ms',
        'codec': 'AC4'
    }),
    ("[2026-02-07 10:15:15] ID:9925 | STATUS:OK | LATENCY:210ms | CODEC:EAC3", {
        'timestamp': '2026-02-07 10:15:15',
        'session_id': '9925',
        'status': 'OK',
        'latency': '210ms',
        'codec': 'EAC3'
    }),
])
def test_extract_log_fields_parametrized(log_line, expected_output):
    assert extract_log_fields(log_line) == expected_output
    

# Practice Pytest, some more variations of the same test function
def test_extract_log_fields_with_invalid_input():
    # Test with completely invalid log line
    invalid_log_line = "This is not a valid log line"
    assert extract_log_fields(invalid_log_line) is None, "Expected None for invalid log line"
    
    # Test with empty string
    empty_log_line = ""
    assert extract_log_fields(empty_log_line) is None, "Expected None for empty log line"
    
    # Test with None input
    assert extract_log_fields(None) is None, "Expected None for None input"
    
# Pytest fixture example
@pytest.fixture
def sample_log_line():
    return "[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms | CODEC:AC4"

def test_extract_log_fields_with_fixture(sample_log_line):
    expected_output = {
        'timestamp': '2026-02-07 10:15:01',
        'session_id': '9922',
        'status': 'OK',
        'latency': '120ms',
        'codec': 'AC4'
    }
    assert extract_log_fields(sample_log_line) == expected_output, "Fixture test failed"
    
# Have a test suite that tests the function with a variety of log lines, including edge cases and invalid inputs. 
# Use assertions to validate the expected output against the actual output from the function.

# Use pytest test suite to run all the test functions and ensure that the extract_log_fields function is working correctly under various scenarios.
# Use pytest fixtures to provide sample log lines for testing.
# Use pytest parametrize to test the function with multiple inputs and expected outputs.
# Use pytest markers to categorize the tests and run specific sets of tests.
# Use pytest plugins to extend the functionality of pytest, such as pytest-cov for code coverage reporting.
# Use pytest configuration files to customize the behavior of pytest, such as pytest.ini or pyproject.toml.
# Use pytest hooks to customize the behavior of pytest, such as pytest_collection_modifyitems to modify the test items before they are collected
# pytest fixtures for setup and teardown of test environments, such as creating temporary files or databases for testing.
# Exampley of using pytest fixtures for setup and teardown
@pytest.fixture
def setup_and_teardown():
    # Setup code: Create a temporary file for testing
    with open('temp_test_file.txt', 'w') as temp_file:
        temp_file.write("This is a temporary test file.\n")
    
    yield  # This is where the test will run
    
    # Teardown code: Remove the temporary file after testing
    import os
    # os.remove('temp_test_file.txt')
# How to use the above fixture in a test function
def test_with_setup_and_teardown(setup_and_teardown):
    # Test code that uses the temporary file created in the fixture
    with open('temp_test_file.txt', 'r') as temp_file:
        content = temp_file.read()
        assert content == "This is a temporary test file.\n", "Content of the temporary file does not match expected value"
        
# Example usage of custom pytest test suite
if __name__ == "__main__":
    pytest.main(["-v", "test_extract_log_fields.py"])