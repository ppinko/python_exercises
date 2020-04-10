"""
Write a Python program to read first n lines of a file.
"""

def read_few_lines(file, n):
    with open (file, mode='r') as reader:
        while True and n > 0:
            line = reader.readline()
            if len(reader.readline()) != 0:
                print(reader.readline(), end='')
                n -= 1
            else:
                break
    
read_few_lines('harry.txt', 10)
