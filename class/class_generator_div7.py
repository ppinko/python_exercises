"""
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.
"""

class Gen7:
    def gene_num_div_7(self, start, end):
        for num in range(start, end + 1):
            if num % 7 == 0:
                yield num