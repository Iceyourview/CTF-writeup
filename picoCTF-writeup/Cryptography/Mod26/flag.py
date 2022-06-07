#! /usr/bin/env python

flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"

AtoZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
atoz = "abcdefghijklmnopqrstuvwxyz"

for i in flag:
    if i in AtoZ:
        print(AtoZ[(AtoZ.index(i)+13)%26],end="")
    elif i in atoz:
        print(atoz[(atoz.index(i)+13)%26],end="")
    else:
        print(i,end="")
