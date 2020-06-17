# https://edabit.com/challenge/Grwj3q6oBfeXxhLq5


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
    return True


def sexy_triplets(low: int, high: int) -> list:
    primes =[i for i in range(low, high + 1) if is_prime(i)]
    triplets = []
    for prime in primes:
        if prime + 12 <= high and is_prime(prime + 6) and is_prime(prime + 12) and not is_prime(prime + 18):
            triplets.append([prime, prime + 6, prime + 12])
    return triplets


assert sexy_triplets(1, 19) == [[7, 13, 19]]
assert sexy_triplets(1, 17) == []
assert sexy_triplets(64, 88) == [[67, 73, 79]]
assert sexy_triplets(11, 59) == [[17, 23, 29], [31, 37, 43], [47, 53, 59]]
assert sexy_triplets(17, 29) == [[17, 23, 29]]
assert sexy_triplets(109, 275) == [[151, 157, 163], [167, 173, 179], [227, 233, 239], [257, 263, 269]]
assert sexy_triplets(1000, 1080) == []
assert sexy_triplets(5842, 6333) == [[6067, 6073, 6079], [6257, 6263, 6269], [6317, 6323, 6329]]
assert sexy_triplets(45000, 45777) == [[45427, 45433, 45439], [45491, 45497, 45503], [45751, 45757, 45763]]

print("Success")