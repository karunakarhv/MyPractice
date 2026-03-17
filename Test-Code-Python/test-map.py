import re
# Map(function, iterables)
list1 = [1, 2, 3, 4]
list2 = ['test?!', 'test!!!!...', 'how are you?']

def removePunctuation(word):
    return re.sub(r'[?!.;"()-]', "", word)

def searchWord(search_file):
    # Using regular expression to search for the word in the file.
    with open(search_file, 'r') as file:
        for line in file:
            if re.search(r'\bword\b', line):
                print(line)
    # What if the file is too large to read into memory? 
    # We can read the file line by line and search for the word in each line. 
    # This way we can handle large files without running into memory issues.
       
    # Read in chunks of the file and search for the word in each chunk. 
    # This can be more efficient than reading the file line by line, 
    # as it reduces the number of I/O operations. 
    # However, it may require more complex logic to handle cases where the word is split across chunk boundaries.
    with open(search_file, 'r') as file:
        chunk_size = 1024  # Adjust the chunk size as needed
        buffer = ""
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            buffer += chunk
            lines = buffer.splitlines()
            for line in lines[:-1]:  # Process all lines except the last one
                if re.search(r'\bword\b', line):
                    print(line)
            buffer = lines[-1]  # Keep the last line in the buffer for the next chunk

def findallWords(search_file):
    with open(search_file, 'r') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content)
        return words
    
print(list(map(lambda x: x * x, list1)))
print(list(map(removePunctuation, list2)))
print(findallWords("sample.txt"))