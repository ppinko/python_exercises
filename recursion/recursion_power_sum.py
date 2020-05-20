

def powerSum(X, N, k, ls):
    # 1 <= X <= 1000
    # 2 <= N <= 10
    count = 0
    boundary = int(X ** (1/N))
    # print(boundary)
    if X == 1:
        count += 1
        print ("HIT")
        # print(X)
        return count
    if boundary ** N == X:
        # print(1, X)
        #print(boundary)
        print("SECOND CHANCE", X)
        count += 1
    for i in range(k, boundary):
        # print(2, X)
        print("INTERMEDIATE", X - i ** N)
        count += powerSum(X - i ** N, N, i+1)
    return count

print(powerSum(25, 2, 1, []))