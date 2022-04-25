#PMCH

from re import S
from Bio import SeqIO
from Bio.Seq import Seq
from math import factorial

for record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_pmch.txt", "fasta"):
    sequence = record.seq
    
#sequence = "AGCUAGUCAU"
match = {"C":"G", "G":"C", "A":"U", "U":"A" }
'''
def matching(s):
    perfect = 1
    for i in range(1, len(s)-1):
        if s[i] == match[s[0]]:
            new_s = s[1:i] + s[i+1:]
            perfect += matching(new_s)
    
    while len(s) > 0:
        for i in range(1, len(s)-1):
            if s[i] == match[s[0]]:
                s = s[1:i]+s[i+1:]
                perfect += matching(s)


    return perfect'''


def matching(s):
    A, C = 0, 0
    for i in s:
        if i == "A":
            A += 1
        elif i == "C":
            C += 1
    matching = factorial(A) * factorial(C)
    return matching

print (matching(sequence))