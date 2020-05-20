"""
https://edabit.com/challenge/kDKNRcmZfRFKxSkjz
"""


def unmix(txt: str) -> str:
    first = txt[::2]
    second = txt[1::2]
    end = ''
    if len(txt) % 2 == 1:
        end = first[-1]
    zipped = zip(second, first)
    return ''.join(j for i in zipped for j in i) + end


print(unmix('badce'))
assert unmix('123456') == '214365'
assert unmix('hTsii  s aimex dpus rtni.g') =='This is a mixed up string.'
assert unmix('badce') =='abcde'
print('Success')