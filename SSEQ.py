#SSEQ

from Bio import SeqIO
from Bio.Seq import Seq

Seqlist = []
for record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_sseq.txt", "fasta"):
    Seqlist.append(record.seq)

#Seqlist = ["ACGTACGTGACG", "GTA"]
main = Seqlist[0]
sub = Seqlist[1]

sublen = len(sub)
index = [0]
while sublen > 0:
    for i, nuc in enumerate(main, start = 1):
        #print (i, nuc)
        if i > index[-1] and sub[0] == nuc:
            index.append(i)
            sublen -= 1 
            sub = sub[1:]
            break

output = ""
for i in range(len(index)-1):
    output += str(index[i+1]) + " "
print (output)