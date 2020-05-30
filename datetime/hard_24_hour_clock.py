"""
https://edabit.com/challenge/hTfzPzgNvf4bGphH8
"""


def convert_time(time: str) -> str:
    if 'AM' in time:
        ans = time.replace('AM', '')
        if ans[:2] == '12':
            ans = '00' + ans[2:]
    else:
        temp = time.replace('PM', '')
        L_temp = temp.split(':')
        L_temp[0] = int(L_temp[0]) + 12
        if L_temp[0] == 24:
            L_temp[0] = '12'
        else:
            L_temp[0] = str(L_temp[0])
        ans = ':'.join(L_temp)
    return ans


assert convert_time("07:05:45PM") == "19:05:45"
assert convert_time("12:40:22AM") == "00:40:22"
assert convert_time("12:45:54PM") == "12:45:54"
assert convert_time("05:32:33PM") == "17:32:33"
assert convert_time("11:59:59PM") == "23:59:59"
assert convert_time("11:59:59AM") == "11:59:59"
assert convert_time("06:00:19AM") == "06:00:19"

print('Success')