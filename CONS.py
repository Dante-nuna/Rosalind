# CONS

from Bio import SeqIO
import numpy as np

first_record = next(SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_cons.txt", "fasta"))
seqlen = len(first_record)
#print(seqlen)

ACGT = [[0 for col in range(seqlen)]for row in range(4)]
#print(ACGT)

with open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_cons.txt") as handle:
    for record in SeqIO.parse(handle,"fasta"):
        for i in range(seqlen):
            if record.seq[i] == 'A':
                ACGT[0][i] += 1
            elif record.seq[i] =='C':
                ACGT[1][i] += 1
            elif record.seq[i] =='G':
                ACGT[2][i] += 1
            else:
                ACGT[3][i] += 1


max = np.argmax(ACGT, axis=0)
dict = {0:"A", 1:"C", 2:"G", 3:"T"}
con = ""
for i in range(seqlen):
    con += dict[max[i]]
print (con)

def listToString(list):
    result = ""
    for s in list:
        result += str(s) + " "
    return result.strip()

print ("A:", listToString(ACGT[0]))
print ("C:", listToString(ACGT[1]))
print ("G:", listToString(ACGT[2]))
print ("T:", listToString(ACGT[3]))
