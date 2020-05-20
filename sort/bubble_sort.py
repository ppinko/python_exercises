"""
for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}

Given an array of integers, sort the array in ascending order using 
the Bubble Sort algorithm above. Once sorted, print the following 
three lines:
1. Array is sorted in numSwaps swaps., where numSwaps is the number of 
swaps that took place.
2. First Element: firstElement, where firstElement is the first element 
in the sorted array.
3. Last Element: lastElement, where lastElement is the last element in 
the sorted array.
"""

def countSwaps(a):
    counter = 0
    flag = True
    while flag:
        temp_swap = 0
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                temp = a[i]
                swap = a[i+1]
                a[i], a[i+1] = swap, temp
                counter += 1
                temp_swap += 1
        if temp_swap == 0:
            flag = False
            
    print("Array is sorted in {0} swaps.".format(counter))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[-1]))