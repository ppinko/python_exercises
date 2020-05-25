

def ile_krol(n: int, x: int, y: int) -> int:
    corners = ((1, 1), (1, n), (n, 1), (n, n))
    if (x, y) in corners:
        return 3
    elif x == 1 or y == 1 or x == n or y == n:
        return 5
    else:
        return 8


print(ile_krol(8, 1, 1))
print(ile_krol(10, 4, 4))