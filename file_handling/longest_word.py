"""
Write a python program to find the longest words.
"""

import string

def longest_word(file):
    with open (file, mode='r') as f:
        max_len = 0
        max_word = ''
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line_no_punct = ''.join(i for i in line if i not in string.punctuation)
            temp_ls = line_no_punct.split()
            for i in temp_ls:
                if len(i) > max_len:
                    max_word = i
                    max_len = len(i)
    return max_word
            
        
print(longest_word('harry.txt'))
