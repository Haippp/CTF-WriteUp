import string
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
binary = "{0:08b}"
key = "abc"
assert all([k in ALPHABET for k in key])

print(LOWERCASE_OFFSET)
print(ALPHABET)
