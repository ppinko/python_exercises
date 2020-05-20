"""
https://edabit.com/challenge/7vN8ZRw43yuWNoy3Y

Encoded String Parse

Create a function which takes in an encoded string and returns a dictionary according to the following example:

Examples:

parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}
"""


def parse_code(encoded: str) -> dict:
    L = [i for i in encoded.split('0') if len(i) > 0];
    d = ['first_name', 'last_name', 'id']
    return dict(zip(d, L))


assert parse_code('John000Doe000123') == {'first_name': 'John', 'last_name': 'Doe', 'id': '123'}
assert parse_code('Michael0Smith004331') == {'first_name': 'Michael', 'last_name': 'Smith', 'id': '4331'}
assert parse_code('Thomas0000Lee0000045553') == {'first_name': 'Thomas', 'last_name': 'Lee', 'id': '45553'}
assert parse_code('a0b01') == {'first_name': 'a', 'last_name': 'b', 'id': '1'}

print('Success')