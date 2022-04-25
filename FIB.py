#FIB
file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/Prob.4/rosalind_fib.txt", "r")
set = file.read().split()
file.close()

def fibo(n, k):
    f_n_2, f_n_1 = 1, 1
    for i in range (n-2):
        f_n_2, f_n_1 =  f_n_1, f_n_2 * k + f_n_1
    return f_n_1

n, k = int(set[0]), int(set[1])

print(fibo(n,k))