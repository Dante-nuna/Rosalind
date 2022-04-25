#MRNA

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_mrna.txt", "r")
ptnseq = file.read().strip('\n')
#ptnseq = "MA"

codon = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/RNA codon table.txt", "r").read().split()
codon_dict = {}
term = []
for i in range(int(len(codon)/2)):
    if codon[2*i+1] in codon_dict:
        codon_dict[codon[2*i+1]] = codon_dict[codon[2*i+1]]+1
    else:
        codon_dict[codon[2*i+1]] = 1

product = 1
for j in range(len(ptnseq)):
    product *= codon_dict[ptnseq[j]]

print((product * codon_dict['Stop']) % 1000000)
