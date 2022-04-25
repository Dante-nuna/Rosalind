#SUBS

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_subs.txt", "r")
twoseq = file.read().split('\n')
file.close()
a, b = twoseq[0], twoseq[1]

# pos_b = a.find(b)
pos_b = ''
for i in range(len(a)-len(b)):
    if a[i:i+len(b)] == b:
        pos_b += str(i+1) + " "
print (pos_b)