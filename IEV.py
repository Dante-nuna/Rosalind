#IEV

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_iev.txt", "r")

poplist = file.read().split()
file.close()
pop = []
for i in range(len(poplist)):
    pop.append(int(poplist[i]))
#print(pop)

dom = 2*(pop[0]) + 2*(pop[1]) + 2*(pop[2]) + 2*(3/4) *(pop[3]) + 2*(1/2)*(pop[4])

print(dom)