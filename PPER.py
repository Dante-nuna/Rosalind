#PPER
from math import factorial

def P(n,k):
    permutation = (factorial(n)/factorial(n-k)) % 1000000
    return int(permutation)

#print(P(21, 7))
print(P(90,9))