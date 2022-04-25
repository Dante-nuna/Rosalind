#GRPF

from Bio import SeqIO

def overlap(file, k):
    with open(file) as handle:
        s = {} #suffix
        t = {} #prefix
        for record in SeqIO.parse(handle, "fasta"):
            s[record.id] = record.seq[-k:]
            t[record.id] = record.seq[:k]
        sur, pre = [], []
        for suffix in s.keys():
            for prefix in t.keys():
                if suffix != prefix and s[suffix] == t[prefix]:
                    sur.append(suffix)
                    pre.append(prefix)
    return sur, pre
#print (overlap("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_grph.txt", 3))
a = overlap("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_grph.txt", 3)[0]
b = overlap("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_grph.txt", 3)[1]

for i in range(len(a)):
    print (a[i] + " " + b[i])


#print (s[0] + " " + t[0])
#print (s[1] + " " + t[1])
#print (s[2] + " " + t[2])