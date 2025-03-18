"""
Word Frequency Counter from a File

Write a Python program that reads a text file, counts the frequency of each word,
and writes the results to an output file.

Steps:
- Read the content of a file named "input.txt".
- Count the occurrences of each word (case-insensitive).
- Write the word frequencies to "output.txt" in descending order of frequency.

Constraints:
- Ignore punctuation (! , . ?) when counting words.
- Sorting should be case-insensitive (e.g., "Hello" and "hello" are the same word).
- Solve it efficiently for large files (Hint: Use a dictionary).

Bonus Challenge:

Modify the program to accept the input and output file names as command-line
arguments instead of hardcoding them.

Example Input (input.txt):
Hello world! This is a test.
Hello again, world.

Expected Output (output.txt):
hello: 2
world: 2
this: 1
is: 1
a: 1
test: 1
again: 1
"""

import string


def word_frequency_counter(input_file: str, output_file: str) -> None:
    """
    Simple implementation of word frequency counter from a file
    """
    word_freq = {}
    with open(input_file, "r") as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = word.strip(string.punctuation)
                word_freq[word] = word_freq.get(word, 0) + 1

    # sort dictionary based on values in descending order and keys in ascending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda item: (-item[1], item[0]))
    with open(output_file, "w") as file:
        for word, freq in sorted_word_freq:
            file.write(f"{word}: {freq}\n")


word_frequency_counter(
    "word_frequency_counter_from_file_in.txt",
    "word_frequency_counter_from_file_out.txt",
)
