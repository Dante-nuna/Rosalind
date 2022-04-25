# Rosalind problems

#s= "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.1/rosalind_dna.txt", "r");
s = file.read()
file.close()

DNA = ['A', 'C', 'G', 'T']
for i in DNA:
    print (s.count(i), end = " ")