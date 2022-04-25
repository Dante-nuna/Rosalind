#t = "GATGGAACTTGACTACGTAAATT"

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.2/rosalind_rna.txt", "r");
t = file.read()
file.close()

u=""
for i in range(len(t)):
    if t[i] == "T":
        u += "U"
    else:
        u += t[i]
    
print (u)