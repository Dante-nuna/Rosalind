#GRPF whynot

from Bio import SeqIO

with open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_grph.txt") as handle:
    out = []
    for sur in SeqIO.parse(handle, "fasta"):
        for pre in SeqIO.parse(handle, "fasta"):
            print (sur.id, pre.id)
'''  
file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_grph.txt", "r")
overlap = SeqIO.parse(file,"fasta")
out = []

id = []
sequence = []
for s in overlap:
    id.append(s.id)
    sequence.append(s.seq)

for i in range(len(id)):
    for j in range(len(id)):
        if  i!= j and sequence[i][-3:] == sequence[j][:3]:
            out.append([id[i], id[j]])

for i in range(len(out)):
    print (out[i][0] + " " + out[i][1])'''