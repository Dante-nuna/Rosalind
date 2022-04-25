#PERM

import itertools

def fact (n):
    prod = 1
    for i in range (1, n+1):
        prod *= i
    return prod

a = int(open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_perm.txt", "r").read())
#a=3

number = []
for i in range (1, a+1):
    number.append(str(i))

permut = list(map(''.join, itertools.permutations(number)))

f = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_perm_output.txt", "w")
f.write(str(fact((a)))+"\n")
for j in range(fact(a)):
    each = ""
    for k in range(len(permut[j])):
        each += permut[j][k] + " "
    f.write(each + "\n")
f.close()



