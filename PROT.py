#PROT

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/RNA codon table.txt", "r")
rna_codon = file.read().split(" ")
rna_dict = {}
file.close()
for i in range(len(rna_codon)-1):
    if i % 2 == 0:
        rna_dict[rna_codon[i]] = rna_codon[i+1]

file2 =  open ("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_prot.txt", "r")
rna_seq = file2.read().strip('\n')
file2.close()
protein_seq = ''
for j in range(0, len(rna_seq), 3):
    protein_seq += str(rna_dict[rna_seq[j:j+3]])
    if rna_dict[rna_seq[j:j+3]] == "Stop":
        protein_seq = protein_seq.replace("Stop", "")
        break
    if j+3 >= len(rna_seq):
        break

print (protein_seq)
