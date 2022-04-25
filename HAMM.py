#HAMM
def d_H(one,two):
    cnt = 0
    for i in range(len(one)):
        if one[i] != two[i]:
            cnt += 1
    return cnt

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.6/rosalind_hamm.txt", "r")
seq = file.read().split('\n')
file.close()

s, t = seq[0], seq[1]

print(d_H(s,t))