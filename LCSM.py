#LCSM
from Bio import SeqIO

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_lcsm.txt", "r")
idlist = []
seqlist =[]
for record in SeqIO.parse(file, "fasta"):
    idlist.append(record.id)
    seqlist.append(record.seq)

file.close()
firstseq = str(seqlist[0])
#print(idlist)
#print(firstseq)

substring = []
for j in range(len(firstseq)-1):
    for k in range(j+1, len(firstseq)):
        substring.append(firstseq[j:k])
#print(substring)

allcontain = []
for l in range(len(substring)):
    a = 0
    for m in range(len(seqlist)):
        if substring[l] not in seqlist[m]:
            a+=1
            break
    if a ==0:
        allcontain.append(substring[l])

maxlength = max([len(x) for x in allcontain])
for i in range(len(allcontain)):
    if len(allcontain[i]) == maxlength:
        print(allcontain[i])