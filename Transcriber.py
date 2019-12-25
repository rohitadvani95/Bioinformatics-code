# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:37:46 2019

@author: kirby
"""


f = open("C://users/kirby/Downloads/rosalind_GC.txt","r")  
DNAseq = ''.join([x.strip('\r\n') for x in f.readlines()]).split('>Rosalind_')

#print(lista)

print(type(DNAseq))


def ListToString(s):
    
    str1 = ""
    
    for ele in s:
        str1 += ele
        
    return str1
s = DNAseq
print(ListToString(s))

RNA_string = s.replace("T","U")

print(RNA_string)
