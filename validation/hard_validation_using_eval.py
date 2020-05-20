"""
https://edabit.com/challenge/ya4diBApyLQKG7TQK
"""


def validate_relationships(expression: str) -> bool:
    new_str = ''
    for i, v in enumerate(expression):
        if v != '=':
            new_str += v
        else:
            if expression[i-1] == '<' or expression[i-1] == '>':
                new_str += v
            else:
                new_str += '=='
    return eval(new_str)


assert validate_relationships("5>-1<0=0<-5>5=5") == False
assert validate_relationships("-15<-10<=0=0<5") == True
assert validate_relationships("0=807<1000<=1000>9990<-3605<=20") == False
assert validate_relationships("3<=3<11>-109") == True
assert validate_relationships("44>-33>=1>-13") == False
assert validate_relationships("10>2=22>9>3") == False
assert validate_relationships("44>0<13>=-2<-1=-1") == True
assert validate_relationships("3>=-1") == True
assert validate_relationships("9<=9<-1") == False
assert validate_relationships("0<9<=9>-1") == True
assert validate_relationships("44>=0<13>-2<-1=1") == False
assert validate_relationships("-39<=5=5<=9>-1") == True
assert validate_relationships("55>7>=7>=1") == True
assert validate_relationships("3<19>-19>5>=-19") == False

print('Success')