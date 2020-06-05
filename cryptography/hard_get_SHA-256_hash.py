"""
https://edabit.com/challenge/haaS4SBv42N3btcg5
"""


import hashlib


def get_sha256_hash(passwd: str) -> str:
    m = hashlib.sha256(passwd.encode())
    return m.hexdigest()


assert get_sha256_hash("hi") == "8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4"
assert get_sha256_hash("password123") == "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
assert get_sha256_hash("don't use easy passwords") == "9fdfef802f06e384101080935fd3c938c60f92f528d520528b5c0491471a2be1"

print('Success')