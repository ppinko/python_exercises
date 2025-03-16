'''
Missing Number in an Array
You are given a list of n distinct numbers taken from the range 0 to n. One 
number is missing. Your task is to find and return the missing number.

Example Input:
nums = [3, 0, 1]

Expected Output:
2
'''

def missing_number_in_array(nums: list[int]) -> int:
    '''
    Simple solution using set and pop method.
    '''
    all_nums = set(range(min(nums), max(nums) + 1))
    return all_nums.difference(nums).pop()

nums = [3, 0, 1]

print(missing_number_in_array(nums))