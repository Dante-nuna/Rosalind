#LONG

from Bio import SeqIO
from Bio.Seq import Seq

seqlist = []
for record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_long.txt", "fasta"):
    seqlist.append(record.seq)

#seqlist = ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"]

nlen = len(seqlist)
eqlen = len(seqlist[0])

def merge (left, right):
    merged = []
    for i in range(eqlen//2, eqlen):
        if left[-i:] == right[:i]:
            merged.append(left + right[i:])
        if left[:i] == right[-i:]:
            merged.append(right + left[i:])
    if merged == []:
        return None
    else:
        return min(merged, key = len)
#print(merge("ATTAGACCTG", "AGACCTGCCG"))

while len(seqlist) > 1:
    shortmerge = []
    for i in seqlist:
        for j in seqlist:
            if i == j : 
                continue
            if merge(i,j) != None:
                sublength = len(i)+len(j)-len(merge(i,j))
                shortmerge.append([merge(i,j), i, j, sublength])
    max_merge = max(shortmerge, key=lambda x: x[3])
    #print(max_merge)
    seqlist.append(max_merge[0])
    seqlist.remove(max_merge[1])
    seqlist.remove(max_merge[2])

print(seqlist[0])