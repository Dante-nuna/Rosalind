#ORF

from unittest.mock import NonCallableMagicMock
from Bio import SeqIO
from Bio.Seq import Seq

with open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_orf.txt", "r") as file:
    tot =  file.read()
    dnaseq = tot.split("\n")[1:-1]
    dnaseq = ("").join(dnaseq)
#print (dnaseq)
#dnaseq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

sixframes = []
mydnaseq = Seq(dnaseq)
comple = mydnaseq.reverse_complement()
#print(str(comple))
for i in range(3):
    sixframes.append(dnaseq[i:((len(dnaseq)-i+1)//3)*3-1])
    sixframes.append(str(comple)[i:((len(dnaseq)-i+1)//3)*3-1])
#print(len(sixframes))

allseq = []
for j in range(6):
    rnaseq = Seq(sixframes[j]).transcribe()
    ptnseq = str(rnaseq.translate())
    allseq.append(ptnseq)

ptn = set()
for k in range(len(allseq)):
    pos = None
    for pos, char in enumerate(allseq[k]):
        thisseq = allseq[k]
        if char == 'M':
            M_pos = pos
            end = thisseq[M_pos:].find('*')
            if end >0:
                ptn.add(allseq[k][M_pos:M_pos+end])

for seq in ptn:
    print(seq)