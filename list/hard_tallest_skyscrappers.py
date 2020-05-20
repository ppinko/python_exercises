"""
https://edabit.com/challenge/76ibd8jZxvhAwDskb
"""

def tallest_skyscraper(lst):
    return max(sum(lst[j][i] for j in range(len(lst))) for i in range(len(lst[0])))

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) == 3)
