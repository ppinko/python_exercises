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

import re
from collections import Counter


def word_frequency_counter_2(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read().lower()  # Convert to lowercase

        # Remove punctuation and split into words
        words = re.findall(r"\b\w+\b", text)

        # Count word occurrences
        word_counts = Counter(words)

        # Sort by frequency (descending) and then alphabetically
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        # Write results to output file
        with open(output_file, "w", encoding="utf-8") as file:
            for word, count in sorted_words:
                file.write(f"{word}: {count}\n")

        print(f"Word frequencies written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print(
            "Usage: python word_frequency_counter_from_file.py input_file output_file"
        )
    else:
        word_frequency_counter_2(sys.argv[1], sys.argv[2])
