"""
https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
"""


def longest_substring(nums: str) -> str:
    temp_max, temp = '', ''
    for i, v in enumerate(nums):
        if temp == '':
            temp += v
        elif int(temp[-1]) % 2 != int(v) % 2:
            temp += v
        else:
            if len(temp) > len(temp_max):
                temp_max = temp
            temp = v
    if len(temp) > len(temp_max):
        temp_max = temp
    return temp_max


assert longest_substring("844929328912985315632725682153") =="56327256"
assert longest_substring("769697538272129475593767931733") =="27212947"
assert longest_substring("937948289456111258444958189244") =="894561"
assert longest_substring("736237766362158694825822899262") =="636"
assert longest_substring("369715978955362655737322836233") =="369"
assert longest_substring("345724969853525333273796592356") =="496985"
assert longest_substring("548915548581127334254139969136") =="8581"
assert longest_substring("417922164857852157775176959188") =="78521"
assert longest_substring("251346385699223913113161144327") =="638569"
assert longest_substring("483563951878576456268539849244") =="18785"
assert longest_substring("853667717122615664748443484823") =="474"
assert longest_substring("398785511683322662883368457392") =="98785"
assert longest_substring("368293545763611759335443678239") =="76361"
assert longest_substring("775195358448494712934755311372") =="4947"
assert longest_substring("646113733929969155976523363762") =="76523"
assert longest_substring("575337321726324966478369152265") =="478369"
assert longest_substring("754388489999793138912431545258") =="545258"
assert longest_substring("198644286258141856918653955964") =="2581418569"
assert longest_substring("643349187319779695864213682274") =="349"
assert longest_substring("919331281193713636178478295857") =="36361"

print('Success')