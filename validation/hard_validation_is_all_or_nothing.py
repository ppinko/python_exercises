"""
https://edabit.com/challenge/26P2iwW5WfwPGJyWE
"""


def possibly_perfect(answers, keys) -> bool:
    L = []
    for i, j in zip(answers, keys):
        if i == j:
            L.append(True)
        elif i == '_':
            continue
        else:
            L.append(False)
    return all(L) or not any(L) or len(L) == 0


assert possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']) == True
assert possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C']) == False
assert possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T']) == True

assert possibly_perfect(['B', 'A', '_', '_'], ['B', 'A', 'C', 'C']) == True
assert possibly_perfect(['A', 'B', 'A', '_'], ['B', 'A', 'C', 'C']) == True
assert possibly_perfect(['A', 'B', 'C', '_'], ['B', 'A', 'C', 'C']) == False

assert possibly_perfect(['B', '_'], ['C', 'A']) == True
assert possibly_perfect(['B', 'A'], ['C', 'A']) == False
assert possibly_perfect(['B'], ['B']) == True

assert possibly_perfect(['_', 'T', '_', '_'], ['T', 'F', 'F', 'F']) == True
assert possibly_perfect(['_', 'T', '_', '_'], ['T', 'T', 'F', 'T']) == True
assert possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'F', 'T']) == False
assert possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']) == True
assert possibly_perfect(['_', 'T', 'T', 'T'], ['F', 'F', 'F', 'F']) == True

print('Success')