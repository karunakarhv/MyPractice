# Practice writing for File Opening, Reading, Writing, and Closing

# Open a file for writing
# file = open('example.txt', 'w')
# # Write some text to the file
# file.write('Hello, this is a practice file.\n')
# file.write('This file is used for practicing file operations in Python.\n')
# # Close the file
# file.close()

# # In Memory File Operations
# from io import StringIO
# # Create an in-memory file-like object
# in_memory_file = StringIO()
# # Write some text to the in-memory file
# in_memory_file.write('This is an in-memory file.\n')
# in_memory_file.write('It behaves like a regular file but is stored in memory.\n')
# # Move the cursor to the beginning of the in-memory file
# in_memory_file.seek(0)
# # Read the content of the in-memory file
# content = in_memory_file.read()
# print(content)
# # Close the in-memory file
# in_memory_file.close()

# Read a large file in chunks
with open('test_log.txt', 'r') as large_file:
    while True:
        chunk = large_file.read(1024)  # Read 1024 bytes at a time
        if not chunk:
            break  # End of file reached
        print(chunk)  # Process the chunk (e.g., print it)