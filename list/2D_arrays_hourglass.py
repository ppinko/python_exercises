""" https://www.hackerrank.com/challenges/2d-array/problem """

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

arr2 = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

def hourglassSum(arr):
    width = 3
    size = len(arr) - width + 1
    for i in range(size):
        for j in range(size):
            val = sum(arr[i][j:width+j]) 
            val += arr[i+1][j+1] 
            val += sum(arr[i+2][j:width+j])
            if i == 0 and j == 0:
                max_value = val
            elif val > max_value:
                max_value = val
    return max_value

print(hourglassSum(arr))
print(hourglassSum(arr2))