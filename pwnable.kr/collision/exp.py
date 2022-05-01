from pwn import *

sh = ssh('col','pwnable.kr', 2222, 'guest')

# hashcode
hashcode = 0x21DD09EC

'''
The input will be checked from argv[1], then enter 'check_password' to calculate the result, and finally return it to main, and then judge whether it is the same as the hashcode, so we need to create the input that is  equal to the hashcode.   
'''
# payload
average = hashcode//5
remainder = hashcode%5

payload = p32(average)*4 + p32(remainder+average)

# process('./col')
sh = sh.process(['col', payload], './col')
sh.interactive()

