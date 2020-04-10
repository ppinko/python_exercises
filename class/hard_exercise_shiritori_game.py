"""


The basic premise is to follow two rules:

    First character of next word must match last character of previous word.
    The word must not have already been said.

Example:
["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!
["motive", "beach"]  # invalid! - beach should start with "e"
["hive", "eh", "hive"]  # invalid! - "hive" has already been said

Write a Shiritori class that has two instance variables:

    words: a list of words already said.
    game_over: a boolean that is true if the game is over.

and two instance methods:

    play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).
        If it is valid, it adds the word to the words list, and returns the words list.
        If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.

    restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

Game example:
my_shiritori = Shiritori()

my_shiritori.play("apple") ➞ ["apple"]
my_shiritori.play("ear") ➞ ["apple", "ear"]
my_shiritori.play("rhino") ➞ ["apple", "ear", "rhino"]
my_shiritori.play("corn") ➞ "game over"

# Corn does not start with an "o".

my_shiritori.words ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart ➞ "game restarted"
my_shiritori.words ➞ []

# Words list should be set back to empty.

my_shiritori.play("hostess") ➞ ["hostess"]
my_shiritori.play("stash") ➞ ["hostess", "stash"]
my_shiritori.play("hostess") ➞ "game over"

# Words cannot have already been said.

Notes

    Note: The play method should not add an invalid word to the words list.
    You don't need to worry about capitalization or white spaces for the inputs for the play method.
    The play method will only take in single arguments as inputs.
    Read more about Shiritori in the Resources tab.

"""

class Shiritori:
    def __init__(self, words = [], game_over = False):
        self.words = words
        self.game_over = game_over

    def play(self, word):
        if (self.words == [] or self.words[-1][-1] == word[0]) and word not in self.words:
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def restart(self):
        self.game_over = False
        self.words = []
        return "game restarted"
        
my_shiritori = Shiritori()

my_shiritori.play("apple") # ["apple"]
my_shiritori.play("ear") # ["apple", "ear"]
my_shiritori.play("rhino") # ["apple", "ear", "rhino"]
my_shiritori.play("corn") # "game over"

# Corn does not start with an "o".

my_shiritori.words # ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart # "game restarted"
my_shiritori.words # []

# Words list should be set back to empty.

my_shiritori.play("hostess") # ["hostess"]
my_shiritori.play("stash") # ["hostess", "stash"]
my_shiritori.play("hostess") # "game over"            
