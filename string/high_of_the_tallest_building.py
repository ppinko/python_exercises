"""
https://edabit.com/challenge/LuBtaT9dwStbd7mnK
"""

def tallest_building_height(lst):
    num_col = len(lst[0])
    num_row = len(lst)
    max_val = 0
    n = 0
    for i in range(num_col):
        temp = 0
        k = num_row - 1
        while k >= 0:
            if lst[k][i] == '#':
                temp += 1
                k -= 1
                if k == -1:
                    max_val = temp
            else:
                if temp > max_val:
                    max_val = temp
                break
        print(max_val)
    return str(max_val * 20) + 'm'

print(tallest_building_height([
	"         ",
	" ##      ",
	" ##      ",
	"###   ## ",
	"###   ## ",
	"###   ###",
	"###   ###"
]))

print(tallest_building_height([
	"            ##",
	"            ##",
	"            ##",
	"###   ###   ##",
	"###   ###   ###",
	"###   ###   ###",
	"###   ###   ###"
]))
