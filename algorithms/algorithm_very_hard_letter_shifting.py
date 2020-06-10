"""
https://edabit.com/challenge/vnzjuqjCf4MFHGLJp
"""


def shift_letters(txt: str, shift: int) -> str:
    without_punc = ''.join(i for i in txt if i.isalpha())
    real_shift = shift % len(without_punc)
    transformed_without_punc = without_punc[len(without_punc) - real_shift:] + without_punc[:len(without_punc) - real_shift]
    ans, k = '', 0
    for i in txt:
        if i == ' ':
            ans += ' '
        else:
            ans += transformed_without_punc[k]
            k += 1
    return ans


assert shift_letters("Made by Harith Shah", 15) == "adeb yH arithS hahM"
assert shift_letters("Boom", 1) == "mBoo"
assert shift_letters("The most addictive way to learn", 19) == "add icti vewaytole arn Th emost"
assert shift_letters("This is a test", 13) == "stTh is i sate"
assert shift_letters("Shift the letters", 1) == "sShif tth eletter"
assert shift_letters("A B C D E F G H", 4) == "E F G H A B C D"
assert shift_letters("Edabit helps you learn in bitesize chunks", 39) == "unksEd abith elp syoul ea rninbite sizech"
assert shift_letters("To be or not to be", 6) == "ot to be Tob eo rn"
assert shift_letters("Made by Harith Shah", 18) == "ahMa de byHari thSh"
assert shift_letters("Boom", 0) == "Boom"
assert shift_letters("The most addictive way to learn", 5) == "lea rnTh emostaddi cti ve wayto"
assert shift_letters("This is a test", 9) == "isis at e stTh"
assert shift_letters("Shift the letters", 3) == "ersSh ift thelett"
assert shift_letters("A B C D E F G H", 10) == "G H A B C D E F"
assert shift_letters("Birds of a Feather Flock Together", 32) == "therB ir d sofaFea therF lockToge"
assert shift_letters("Talk the Talk", 1) == "kTal kth eTal"


print("Succes")