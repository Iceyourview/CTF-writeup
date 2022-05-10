# Try it
```
passcode@pwnable:~$ ls
flag  passcode  passcode.c
passcode@pwnable:~$ ./passcode
Toddler's Secure Login System 1.0 beta.
enter you name : AAAA
Welcome AAAA!
enter passcode1 : AAAA
enter passcode2 : checking...
Login Failed!
passcode@pwnable:~$ AAAA
AAAA: command not found
passcode@pwnable:~$ ./passcode
Toddler's Secure Login System 1.0 beta.
enter you name : AAAA
Welcome AAAA!
enter passcode1 : 1234
Segmentation fault (core dumped)

```
We can see that the program asks us to enter name, passcode1, passcode2.
* name
* passcode1
* passcode2

Let's see the program(passcode.c).
```c
#include <stdio.h>
#include <stdlib.h>

void login(){
    int passcode1;
    int passcode2;

    printf("enter passcode1 : ");
    scanf("%d", passcode1);
    fflush(stdin);

    // ha! mommy told me that 32bit is vulnerable to bruteforcing :)
    printf("enter passcode2 : ");
        scanf("%d", passcode2);

    printf("checking...\n");
    if(passcode1==338150 && passcode2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
      exit(0);
        }
}

void welcome(){
    char name[100];
    printf("enter you name : ");
    scanf("%100s", name);
    printf("Welcome %s!\n", name);
}

int main(){
    printf("Toddler's Secure Login System 1.0 beta.\n");

    welcome();
    login();

    // something after login...
    printf("Now I can safely trust you that you have credential :)\n");
    return 0;
}

```

In additional to **main** , the program include other function.
* **welcome**
	```
	void welcome(){
   		char name[100];
   		printf("enter you name : ");
    		scanf("%100s", name);
    		printf("Welcome %s!\n", name);
	}

	```
* **login**
	```
	void login(){
            int passcode1;
            int passcode2;

            printf("enter passcode1 : ");
            scanf("%d", passcode1);
            fflush(stdin);

            // ha! mommy told me that 32bit is vulnerable to bruteforcing :)
    	    printf("enter passcode2 : ");
            scanf("%d", passcode2);

            printf("checking...\n");
            if(passcode1==338150 && passcode2==13371337){
                    printf("Login OK!\n");
                    system("/bin/cat flag");
            }
            else{
                    printf("Login Failed!\n");
            exit(0);
            }
        }

	```
It can found that the variables in scanf are less **&**.
* scanf(format)
	```c
	int scanf(const char *format, Object *arg(s))
	```
When **scanf** is executed, the value of the variable will be written as address.

# Analysis
Using **gdb**

* **main**
	```
	passcode@pwnable:~$ gdb passcode -q
	Reading symbols from passcode...(no debugging symbols found)...done.
	(gdb) disas main
	Dump of assembler code for function main:
   	0x08048665 <+0>:     push   %ebp
   	0x08048666 <+1>:     mov    %esp,%ebp
   	0x08048668 <+3>:     and    $0xfffffff0,%esp
        0x0804866b <+6>:     sub    $0x10,%esp                       
   	0x0804866e <+9>:     movl   $0x80487f0,(%esp)
   	0x08048675 <+16>:    call   0x8048450 <puts@plt>
  	0x0804867a <+21>:    call   0x8048609 <welcome>
   	0x0804867f <+26>:    call   0x8048564 <login>
   	0x08048684 <+31>:    movl   $0x8048818,(%esp)
   	0x0804868b <+38>:    call   0x8048450 <puts@plt>
   	0x08048690 <+43>:    mov    $0x0,%eax
   	0x08048695 <+48>:    leave  
   	0x08048696 <+49>:    ret    
	End of assembler dump.
	```
* **welcome**
	```
	(gdb) disas welcome
	Dump of assembler code for function welcome:
   	0x08048609 <+0>:     push   %ebp
   	0x0804860a <+1>:     mov    %esp,%ebp
   	0x0804860c <+3>:     sub    $0x88,%esp
   	0x08048612 <+9>:     mov    %gs:0x14,%eax
   	0x08048618 <+15>:    mov    %eax,-0xc(%ebp)        
   	0x0804861b <+18>:    xor    %eax,%eax
   	0x0804861d <+20>:    mov    $0x80487cb,%eax
   	0x08048622 <+25>:    mov    %eax,(%esp)
   	0x08048625 <+28>:    call   0x8048420 <printf@plt>
   	0x0804862a <+33>:    mov    $0x80487dd,%eax
   	0x0804862f <+38>:    lea    -0x70(%ebp),%edx
   	0x08048632 <+41>:    mov    %edx,0x4(%esp)
   	0x08048636 <+45>:    mov    %eax,(%esp)
   	0x08048639 <+48>:    call   0x80484a0 <__isoc99_scanf@plt>
   	0x0804863e <+53>:    mov    $0x80487e3,%eax
   	0x08048643 <+58>:    lea    -0x70(%ebp),%edx        ; notice ebp
   	0x08048646 <+61>:    mov    %edx,0x4(%esp)
   	0x0804864a <+65>:    mov    %eax,(%esp)
   	0x0804864d <+68>:    call   0x8048420 <printf@plt>
   	0x08048652 <+73>:    mov    -0xc(%ebp),%eax
   	0x08048655 <+76>:    xor    %gs:0x14,%eax
   	0x0804865c <+83>:    je     0x8048663 <welcome+90>
   	0x0804865e <+85>:    call   0x8048440 <__stack_chk_fail@plt>
   	0x08048663 <+90>:    leave  
   	0x08048664 <+91>:    ret    
	End of assembler dump.

	```
* **login**
	```
	(gdb) disas login
	Dump of assembler code for function login:
 	0x08048564 <+0>:     push   %ebp
   	0x08048565 <+1>:     mov    %esp,%ebp
   	0x08048567 <+3>:     sub    $0x28,%esp
   	0x0804856a <+6>:     mov    $0x8048770,%eax
   	0x0804856f <+11>:    mov    %eax,(%esp)
   	0x08048572 <+14>:    call   0x8048420 <printf@plt>
   	0x08048577 <+19>:    mov    $0x8048783,%eax
   	0x0804857c <+24>:    mov    -0x10(%ebp),%edx        ; notice ebp
   	0x0804857f <+27>:    mov    %edx,0x4(%esp)
   	0x08048583 <+31>:    mov    %eax,(%esp)
   	0x08048586 <+34>:    call   0x80484a0 <__isoc99_scanf@plt>
   	0x0804858b <+39>:    mov    0x804a02c,%eax
   	0x08048590 <+44>:    mov    %eax,(%esp)
   	0x08048593 <+47>:    call   0x8048430 <fflush@plt>
   	0x08048598 <+52>:    mov    $0x8048786,%eax
   	0x0804859d <+57>:    mov    %eax,(%esp)
   	0x080485a0 <+60>:    call   0x8048420 <printf@plt>
   	0x080485a5 <+65>:    mov    $0x8048783,%eax
   	0x080485aa <+70>:    mov    -0xc(%ebp),%edx         ; notice ebp 
   	0x080485ad <+73>:    mov    %edx,0x4(%esp)
   	0x080485b1 <+77>:    mov    %eax,(%esp)
   	0x080485b4 <+80>:    call   0x80484a0 <__isoc99_scanf@plt>
   	0x080485b9 <+85>:    movl   $0x8048799,(%esp)
   	0x080485c0 <+92>:    call   0x8048450 <puts@plt>
   	0x080485c5 <+97>:    cmpl   $0x528e6,-0x10(%ebp)
   	0x080485cc <+104>:   jne    0x80485f1 <login+141>
   	0x080485ce <+106>:   cmpl   $0xcc07c9,-0xc(%ebp)
   	0x080485d5 <+113>:   jne    0x80485f1 <login+141>
   	0x080485d7 <+115>:   movl   $0x80487a5,(%esp)
	```
According three **notice ebp**, we can find out where the variable are, then use the the relatively address of each variable.
Because all function(welcome, login) have no parameters, the ebp will be the same.
# Getting the flag
Overwrite fflush or printf... 
* Overtie GOT
	* fflush
	* printf
