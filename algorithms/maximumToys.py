"""
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    n = 0
    toys = 0
    for price in prices:
        if n + price <= k:
            n += price
            toys += 1
        else:
            return toys