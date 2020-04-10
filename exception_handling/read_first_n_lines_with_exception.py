"""
Write a Python program to read first n lines of a file
with catching potential exception
"""

def read_few_lines(file, n):
    try:
        f = open(file, mode='r') 
    except FileNotFoundError:
        print("File was not found")
    else:
        while True and n > 0:
            line = f.readline()
            if len(f.readline()) != 0:
                print(f.readline(), end='')
                n -= 1
            else:
                f.close()
                break
    finally:
        print("End of the program")
    
read_few_lines('harry.txt', 10)
