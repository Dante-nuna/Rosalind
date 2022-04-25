#LIA

from math import comb
file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_lia.txt", "r")
strset = file.read().split()
set = [int(strset[0]), int(strset[1])]
def Mendel(k, N):
    prob = 0
    for i in range (N, 2**k+1):
        prob += comb(2**k, i) * ((1/4)**i) * ((3/4)**(2**k-i))
    return prob
  
print (Mendel(set[0], set[1]))

'''
import math

def nCr(n, r):
    fac = math.factorial
    return fac(n) / (fac(r)*fac(n-r))

def Mendel_2(k, N):
    prob = 0
    for i in range(N, 2**k+1):
        prob += nCr(2**k, i) * (0.25**i) *(0.75 **(2**k-i))
    return prob
print (Mendel_2(2,1))
'''