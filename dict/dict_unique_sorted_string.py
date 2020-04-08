"""
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the 
words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

def sort_string():
    inp = input("Please enter a sentence: ").split()
    dic = {}
    for element in inp:
        if dic.get(element, 0) == 0:
            dic[element] = 1
    ans = list(dic.keys())
    ans.sort()
    print(" ".join(ans))

sort_string()

"""
# Alternative Solution
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
"""