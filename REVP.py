#REVP

from Bio import SeqIO
from Bio.Seq import Seq

for record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_revp.txt", "fasta"):
    seq = record.seq
len = len(seq)
for i in range(0, len):
    for j in range(i+4, len+1):
        revpan = seq[i:j]
        revcom = revpan.reverse_complement()
        if revpan == revcom and j-i <= 12 and (j-i) % 2==0:
            print(i+1, j-i)



