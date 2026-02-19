---
title: "Powerful Command Line Options in Pytest"
datePublished: Thu Sep 21 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmts055p00050am95seeek50
slug: powerful-command-line-options-in-pytest
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1695297726035/8bfe7232-12ce-49c0-a368-f31715bbc3e5.jpeg
tags: python, python-beginner

---

Pytest provides a variety of command-line options that allow you to customize how your tests are run and reported. These options can be very useful in different testing scenarios. Here are some commonly used command-line options in Pytest:

1. **Specifying Test Files or Directories:**
    
    * `pytest [path]`: Run tests in the specified file or directory. If no path is provided, Pytest will discover and run tests in the current directory and its subdirectories.
        
2. **Running Specific Tests:**
    
    * `pytest test_module.py::test_function`: Run a specific test function within a test module.
        
    * `pytest -k expression`: Run tests that match the provided keyword expression. For example, `-k "important and not slow"` will run tests with both "important" and "not slow" in their names.
        
3. **Markers:**
    
    * `pytest -m marker_name`: Run tests that are marked with a specific marker. For example, `-m slow` will run tests marked as "slow."
        
4. **Output Options:**
    
    * `pytest --verbose (-v)`: Increase verbosity, providing more details about the tests being run.
        
    * `pytest --quiet (-q)`: Decrease verbosity, showing only test outcomes.
        
    * `pytest --color yes/no/auto`: Enable or disable colored output.
        
    * `pytest --tb=style`: Set the traceback style for tracebacks on test failure. Styles include `short`, `line`, `native`, and `no`.
        
5. **Test Selection:**
    
    * `pytest --collect-only`: Show which tests would be collected without running them.
        
    * `pytest --last-failed`: Run the tests that failed during the last test run.
        
    * `pytest --failed-first`: Run the previously failed tests before running any other tests.
        
6. **Parallel Execution:**
    
    * `pytest -n NUM`: Run tests in parallel using multiple processes. For example, `-n 4` will run tests using four processes.
        
7. **Code Coverage:**
    
    * `pytest --cov=package_name`: Measure code coverage for the specified package.
        
    * `pytest --cov-report=type`: Generate code coverage reports in various formats (e.g., `term`, `html`, `xml`).
        
8. **Skipping and Marking Tests:**
    
    * `pytest -k "not slow"`: Skip tests that match a keyword expression. This can be useful to exclude specific tests.
        
    * `pytest -m "not slow"`: Skip tests marked with a specific marker.
        
9. **Test Duration:**
    
    * `pytest --durations=N`: Show the N slowest test durations after the test run.
        
10. **Fixture Debugging:**
    
    * `pytest --setup-show`: Show fixture setup information for each test.
        
11. **Using Config Files:**
    
    * `pytest -c config_file`: Load configuration from a specific config file.
        
12. **Custom Test Discovery:**
    
    * `pytest --collect-only`: Display all discovered tests without running them. Useful for inspecting which tests Pytest has discovered.
        

These are just some of the commonly used command-line options in Pytest. Pytest provides a comprehensive set of options to cater to various testing needs and scenarios. You can run `pytest --help` in your terminal to see a full list of available command-line options and their descriptions.