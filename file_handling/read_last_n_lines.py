"""
Write a Python program to read last n lines of a file.
"""

def read_last_n_lines(file, n):
    with open (file, mode='r') as f:
        ls = list()
        while True:
            l = f.readline()
            if len(l) == 0:
                break
            ls.append(l)
    for line in ls[len(ls) - n:]:
        print(line, end='')

read_last_n_lines("harry.txt", 10)
        
