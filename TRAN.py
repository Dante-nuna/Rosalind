#TRAN

#Transition = Ts = A<->G or T<->C
#Transversion = Tv = (A,G)<->(T<->C)

from Bio import SeqIO
from Bio.Seq import Seq

seqlist = []
for record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_tran.txt", "fasta"):
    seqlist.append(record.seq)

s_1, s_2 = seqlist[0], seqlist[1]
'''s_1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s_2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"
'''
length = len(s_1)

Nuc = {"A" : "purine", "G" : "purine", "C" : "pyrimidine", "T" : "pyrimidine"}

def TsTv(nuc1, nuc2):
    if nuc1 == nuc2:
        return None
    else:
        if Nuc[nuc1] == Nuc[nuc2]:
            return "Ts"
        else:
            return "Tv"

Ts, Tv = 0, 0
for i in range (length):
    if TsTv(s_1[i], s_2[i]) == "Ts":
        Ts += 1
    elif TsTv(s_1[i], s_2[i]) == "Tv":
        Tv += 1

print(float(Ts/Tv))
