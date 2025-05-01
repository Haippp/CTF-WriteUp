import base64

encode_text = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"

print(base64.b64decode(encode_text).decode('utf-8'))
#output : CTF{FlaggyWaggyRaggy}