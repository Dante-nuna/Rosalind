
#s = "AAAACCCGGT"
file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.3/rosalind_revc.txt", "r")
s = file.read().strip() 
'''이렇게 써도 되는지??'''
file.close()

S = ""

reverse = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
for i in range(1, len(s)+1):
    S += reverse[s[-i]]

print (S)