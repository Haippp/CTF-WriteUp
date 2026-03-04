def xor(text, key):
    return bytes(t ^ k for t, k in zip(text, key))

iv, ct = ['391e95a15847cfd95ecee8f7fe7efd66', '8473dcb86bc12c6b6087619c00b6657e']

known_pt = b'FIRE_NUKES_MELA!'
fake_pt = b'SEND_NUDES_MELA!'

iv_new = xor(xor(known_pt, fake_pt), bytes.fromhex(iv)).hex()
print(f'flag{{{iv_new},{ct}}}')