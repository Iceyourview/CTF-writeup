#! /usr/bin/env python

#t =('0','A','B','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
flag = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']

#i = int(input())


for i in flag:
    if(i == '{') :
        print('{',end='')
    elif(i == '}'):
        print('}',end='')
    else:
        print(chr(i+64),end='') 


