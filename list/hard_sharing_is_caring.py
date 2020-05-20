"""
https://edabit.com/challenge/pqpkRBP4YT5dwBDHm
"""


def show_the_love(lst: list) -> list:
    min_lst = min(lst)
    min_ind = lst.index(min_lst)
    ans = lst[:]
    for i, v in enumerate(lst):
        if i == min_ind:
            continue
        elif v % 4 == 0:
            ans[min_ind] += lst[i] // 4
            ans[i] = lst[i] // 4 * 3
        else:
            ans[min_ind] += lst[i] / 4
            ans[i] = lst[i] / 4 * 3
    return ans


assert show_the_love([4, 1, 4]) == [3, 3, 3]
assert show_the_love([16, 10, 8]) == [12, 7.5, 14.5]
assert show_the_love([2, 100]) == [27, 75]
assert show_the_love([75, 64, 55]) == [56.25, 48.0, 89.75]
assert show_the_love([84, 94, 26, 80, 16]) == [63.0, 70.5, 19.5, 60.0, 87.0]
assert show_the_love([55, 27]) == [41.25, 40.75]
assert show_the_love([13, 80, 75, 45, 11]) == [9.75, 60.0, 56.25, 33.75, 64.25]
assert show_the_love([48, 28, 18]) == [36.0, 21.0, 37.0]
assert show_the_love([17, 9]) == [12.75, 13.25]
assert show_the_love([38, 23, 31, 16]) == [28.5, 17.25, 23.25, 39.0]
assert show_the_love([54, 62, 59]) == [84.25, 46.5, 44.25]
assert show_the_love([44, 46]) == [55.5, 34.5]
assert show_the_love([21, 97, 45, 58]) == [71.0, 72.75, 33.75, 43.5]
assert show_the_love([43, 9]) == [32.25, 19.75]
assert show_the_love([53, 0, 14, 58]) == [39.75, 31.25, 10.5, 43.5]
assert show_the_love([16, 19, 42, 43, 6]) == [12.0, 14.25, 31.5, 32.25, 36.0]
assert show_the_love([26, 17, 28, 31, 79]) == [19.5, 58.0, 21.0, 23.25, 59.25]
assert show_the_love([47, 57, 18, 2, 72]) == [35.25, 42.75, 13.5, 50.5, 54.0]
assert show_the_love([27, 77]) == [46.25, 57.75]
assert show_the_love([22, 52]) == [35.0, 39.0]
assert show_the_love([85, 49, 60, 78, 6]) == [63.75, 36.75, 45.0, 58.5, 74.0]
assert show_the_love([96, 38]) == [72.0, 62.0]
assert show_the_love([29, 73, 81]) == [67.5, 54.75, 60.75]
assert show_the_love([51, 46, 81, 85]) == [38.25, 100.25, 60.75, 63.75]
assert show_the_love([26, 48, 84, 70, 8]) == [19.5, 36.0, 63.0, 52.5, 65.0]
assert show_the_love([69, 64]) == [51.75, 81.25]
assert show_the_love([33, 26, 39, 58]) == [24.75, 58.5, 29.25, 43.5]
assert show_the_love([4, 51, 66]) == [33.25, 38.25, 49.5]
assert show_the_love([0, 52, 83, 55, 40]) == [57.5, 39.0, 62.25, 41.25, 30.0]
assert show_the_love([39, 3, 36, 52, 25]) == [29.25, 41.0, 27.0, 39.0, 18.75]
assert show_the_love([32, 78, 12]) == [24.0, 58.5, 39.5]
assert show_the_love([75, 51, 24]) == [56.25, 38.25, 55.5]
assert show_the_love([42, 21, 93, 47]) == [31.5, 66.5, 69.75, 35.25]
assert show_the_love([72, 97, 26, 1]) == [54.0, 72.75, 19.5, 49.75]
assert show_the_love([90, 45, 12]) == [67.5, 33.75, 45.75]
assert show_the_love([37, 47, 82]) == [69.25, 35.25, 61.5]
assert show_the_love([54, 11]) == [40.5, 24.5]
assert show_the_love([78, 86, 19, 46, 51]) == [58.5, 64.5, 84.25, 34.5, 38.25]
assert show_the_love([7, 31, 74, 69]) == [50.5, 23.25, 55.5, 51.75]
assert show_the_love([100, 26, 3, 28, 19]) == [75.0, 19.5, 46.25, 21.0, 14.25]
assert show_the_love([87, 29, 92, 57]) == [65.25, 88.0, 69.0, 42.75]
assert show_the_love([64, 24]) == [48.0, 40.0]
assert show_the_love([82, 89, 52, 25, 50]) == [61.5, 66.75, 39.0, 93.25, 37.5]
assert show_the_love([90, 17, 11]) == [67.5, 12.75, 37.75]
assert show_the_love([14, 24, 27]) == [26.75, 18.0, 20.25]
assert show_the_love([21, 4]) == [15.75, 9.25]
assert show_the_love([70, 64, 25, 16]) == [52.5, 48.0, 18.75, 55.75]
assert show_the_love([50, 17, 87, 20]) == [37.5, 56.25, 65.25, 15.0]
assert show_the_love([60, 27, 56]) == [45.0, 56.0, 42.0]
assert show_the_love([99, 21]) == [74.25, 45.75]
assert show_the_love([80, 0, 45, 84]) == [60.0, 52.25, 33.75, 63.0]

print('Success')