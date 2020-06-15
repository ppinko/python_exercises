""" https://edabit.com/challenge/kiGRxYGqzhoj9Gmit """


morse_to_dots = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
    ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-",
    "-": "-....-", "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-."
}


def decode_morse(code: str) -> str:
    global morse_to_dots
    reversed_dict = dict(zip(morse_to_dots.values(), morse_to_dots.keys()))
    words = code.split('   ')
    return ' '.join([ ''.join([reversed_dict[char] for char in word.split()]) for word in words])


assert decode_morse(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .") == "EDABBIT CHALLENGE"
assert decode_morse(".... . .-.. .--.   -- .   -.-.--") == "HELP ME !"
assert decode_morse("-.-. .... .- .-.. .-.. . -. --. .") == "CHALLENGE"
assert decode_morse(".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-") == "1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."
assert decode_morse("-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..") == "DID YOU GOT MY MAIL ?"
assert decode_morse("- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.") == "TWO THINGS TO KNOW : I FORGET THEM :C"

print("Success")