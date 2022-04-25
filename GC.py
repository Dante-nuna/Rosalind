#GC
from Bio import SeqIO
from Bio.SeqUtils import GC

gc = {}
for seq_record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.5/rosalind_gc.txt", "fasta"):
    c = 0
    #c = 100*(seq_record.seq.count("G") +seq_record.seq.count("C"))/len(seq_record.seq)
    id = seq_record.id
    gc[id] = GC(seq_record.seq)

print (max(gc, key=gc.get))
#print([k for k,v in gc.items() if max(gc.values()) == v])
print (gc[max(gc, key=gc.get)])