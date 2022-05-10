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
passcode@pwnable:~$ cat passcode.c 
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
* welcome
	```
	void welcome(){
   		char name[100];
   		printf("enter you name : ");
    		scanf("%100s", name);
    		printf("Welcome %s!\n", name);
	}

	```
* login
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

# Analysis
Using **gdb**

* main
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

