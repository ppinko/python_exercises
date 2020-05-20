"""
Write a Python program to copy the contents of a file to another file.
"""

def copy_file(old, new):
    with open (old, mode='r') as reader, open (new, mode='w') as writer:
        while True:
            line = reader.readline()
            if len(line) == 0:
                break
            writer.write(line)

copy_file("harry.txt", "copy_file.txt")
