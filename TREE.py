#TREE

f = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_tree.txt", "r")
s = f.read().split("\n")
n = int(s[0])

edge = len(s)-1

print(n-edge)