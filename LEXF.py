#LEXF
from itertools import product

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_lexf.txt", "r")
lines = file.read().split()
items, n = lines[:-1], int(lines[-1])
#print(items, n)
file.close()
#items = ["A", "C", "G", "T"]
#n=2
alllist = []

alllist= list(product(items,repeat = n))
#print (alllist)
strlist = []

for i in range(len(alllist)):
    strlist.append(','.join(alllist[i]))
    strlist[i] = strlist[i].replace(",", "")

print(*strlist, sep='\n') # unpacking operator *