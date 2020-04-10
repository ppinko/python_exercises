"""
Write a Python program to append text to a file and display the text.
"""

def append_text(file, text):
    with open (file, mode='a') as f:
        f.write(text)

s = "\nThis exercise is interesting\nDon't you think?\n"

append_text("harry.txt", s) 
