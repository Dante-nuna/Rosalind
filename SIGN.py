#SIGN

import itertools
n = int(open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_sign.txt", "r").read())
#n=3

permut = []
sign = [-1, 1]
allsign = []
allnumber = []

for j in range(1, n+1):
    allsign.append([(-1)*j, j])

#print (allsign)

onlynumber = list(itertools.permutations(allsign,n))
print(onlynumber)
for i in onlynumber:
    outcome = [str(i[0][0]), str(i[0][1])]
    for j in range(1, n):
        cnt = len(outcome)
        outcome = outcome*2
        for k in range(cnt):
            outcome[k] += " " + str(i[j][0]) 
            outcome[k+cnt] += " " + str(i[j][1])

    permut.append(outcome)

number = 0
for i in range(len(permut)):
    for j in range(len(permut[i])):
        number += 1
    
print(str(number))
        
for i in range(len(permut)):
    for j in range(len(permut[i])):
        number += 1
        print(permut[i][j])