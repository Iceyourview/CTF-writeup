Run it.
```
$ ./flag                                                                                             
I will malloc() and strcpy the flag there. take it.
```

First, we look the file using **```file```** .
```
$ file flag                                                                                          
flag: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
```
Then, we using **```gdb```**...
```
$ gdb flag -q                                                                                        
Reading symbols from flag...
(No debugging symbols found in flag)
gdb-peda$ info fun
All defined functions:

```
No any function in the file? \
One of the reason that the binary file has  any function could be it is packed.
	* Upx
# Unpack 
[Upx](https://en.wikipedia.org/wiki/UPX)
```
$ upx -d flag -o flag_noUpx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag_noUpx

Unpacked 1 file.
```
# Try to get the flag
Using **```gdb```** .
```
gdb-peda$ info fun
All defined functions:

Non-debugging symbols:
0x00000000004002f8  _init
0x00000000004003d0  check_one_fd.part
0x0000000000400441  munmap_chunk.part
0x0000000000400455  group_number
0x0000000000400557  _i18n_number_rewrite
0x000000000040073c  _i18n_number_rewrite
0x0000000000400921  is_trusted_path_normalize
0x0000000000400a1a  print_search_path
0x0000000000400b69  strip
...
```
We can see all defined functions was shown in the list.
1. Set main to break point.
2. Run the program.
3. Using **```ni```** to analysis.

 
We can see the flag in 0x6c2070.
```
UPX...? sounds like a delivery service :)
```
