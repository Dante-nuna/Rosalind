#IPRB

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.7/rosalind_iprb.txt", "r")
org = file.read().split(' ')
k, m, n = int(org[0]), int(org[1]), int(org[2])
tot = k + m + n

#prob = (k*(tot-1)+ + m*(m-1)*3/4 + m*n*1/2)/(tot*(tot-1))
prob = 1 - (m/tot)*((m-1)/(tot-1))*(1/4) - ((m/tot)*(n/(tot-1)))*(1/2)*2 - (n/tot)*((n-1)/(tot-1))
print(prob)