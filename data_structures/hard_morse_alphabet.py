"""
https://edabit.com/challenge/tbEwDviZBadDSeGSz
"""


def morse(txt):
    d = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
         "F":"..-.","G":"--.","H":"....","I":"..","J":".---",
         "K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
         "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
         "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
         " ":"....."}
    if txt[0].isalpha():
        txt = txt.upper()
        return ' '.join([d[i] for i in txt])
    d_reversed = dict(zip(d.values(), d.keys()))
    return ''.join([d_reversed[i] for i in txt.split()])


assert morse("Barack Obama") == "-... .- .-. .- -.-. -.- ..... --- -... .- -- .-"
assert morse("Bill Clinton") == "-... .. .-.. .-.. ..... -.-. .-.. .. -. - --- -."
assert morse("George Washington") == "--. . --- .-. --. . ..... .-- .- ... .... .. -. --. - --- -."
assert morse("Benjamin Franklin") == "-... . -. .--- .- -- .. -. ..... ..-. .-. .- -. -.- .-.. .. -."
assert morse("..-. .-. .. . -.. .-. .. -.-. .... ..... ... -.-. .... .. .-.. .-.. . .-.") == "FRIEDRICH SCHILLER"
assert morse(".--- --- .... .- -. -. ..... .-- --- .-.. ..-. --. .- -. --. ..... ...- --- -. ..... --. --- . - .... .") == "JOHANN WOLFGANG VON GOETHE"
assert morse(".--. . - . .-. ..... .... .- -. -.. -.- .") == "PETER HANDKE"

print('Success')