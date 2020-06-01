"""
https://edabit.com/challenge/tA2XfGGZiscWb3q9S
"""


import re


def youtube_id(link: str) -> str:
    t1 = re.search(r'(?<=v=)[^&]+', link)
    if t1 is not None:
        return t1.group()
    t2 = re.search(r'\w+$', link)
    return t2.group()

assert youtube_id('https://www.youtube.com/watch?v=XPEr1cArWRg') == 'XPEr1cArWRg'
assert youtube_id('http://www.youtube.com/watch?v=-SNQGyVW_YI&t=8871') == '-SNQGyVW_YI'
assert youtube_id('https://youtube.com/watch?t=4m40s&v=vxP3bY-XxY4') == 'vxP3bY-XxY4'
assert youtube_id('www.youtube.com/watch?list=PL3QZUm48uWnsdFakp3A2fI-NzmfH1jyQe&v=yv56ncTdTmU&index=8') == 'yv56ncTdTmU'
assert youtube_id('https://youtu.be/BCDEDi5gDPo') == 'BCDEDi5gDPo'
assert youtube_id('https://www.youtube.com/watch?feature=youtu.be&v=jOxnoDi9IYg&t=3311s') == 'jOxnoDi9IYg'
assert youtube_id('https://www.youtube-nocookie.com/embed/2w9SQjdn9U4') == '2w9SQjdn9U4'

print("Success")