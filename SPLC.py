#SPLC
from Bio import SeqIO
from Bio.Seq import Seq

dna_list = []
for record in SeqIO.parse("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_splc.txt", "fasta"):
    dna_list.append(record.seq)

#dna_list = ["ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG", "ATCGGTCGAA", "ATCGGTCGAGCGTGT"]
rna = ""
exon = ""
for i in range(1, len(dna_list)):
    dna_list[0] = dna_list[0].replace(dna_list[i],"")
    
#print(dna_list[0])

rna = Seq(dna_list[0]).transcribe()
exon = rna.translate()
print(exon.replace("*", ""))
    