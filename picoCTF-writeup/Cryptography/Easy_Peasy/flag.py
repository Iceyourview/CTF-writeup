from pwn import *

r = remote("mercury.picoctf.net", 64260)
r.recvline()
r.recvline()

flag_enc = bytes.fromhex(r.recvline().decode())
fl = len(flag_enc)


def enc(m):
    r.sendlineafter(b"What data would you like to encrypt? ", m)
    r.recvline()
    return bytes.fromhex(r.recvline().decode())


enc("a" * (50000 - fl))
keyxor = enc("a" * fl)

success('keyxor = '+ str(keyxor))

def xor(x, y):
    return bytes(a ^ b for a, b in zip(x, y))


key = xor(keyxor, b"a" * fl)
flag = xor(flag_enc, key)
print("picoCTF{%s}" % flag.decode())