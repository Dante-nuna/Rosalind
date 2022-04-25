#PROB

import math

f = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_prob.txt", "r")
file = f.read().split("\n")
s = file[0]
array = file[1].split(" ")
A = []
for i in array:
    A.append(float(i))

B = []
for gc in A:
    ntprob = {}
    ntprob["A"], ntprob["T"] = (1-gc)/2, (1-gc)/2
    ntprob["G"], ntprob["C"] = gc/2, gc/2
    
    outcome = 0
    for nt in s:
        outcome += float(math.log10(ntprob[nt]))
    B.append(round(outcome,3))

strB = ""
for i in B:
    strB += str(i) + " "
print(strB)