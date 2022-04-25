#PRTM

file = open ("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_prtm.txt", "r")
protein = file.read().replace('\n', '')
#protein = "SKADYEK"

reffile = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/monoisotopic mass table.txt", "r")
massfile = reffile.read().split()
mass = {}
for i in range(len(massfile)//2):
    mass[massfile[2*i]] = float(massfile[2*i+1])

tot = 0
for i in range (len(protein)):
    tot += mass[protein[i]]

print(tot)