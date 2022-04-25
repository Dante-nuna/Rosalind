#FIBD

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_fibd.txt", "r")
set = file.read().split()
file.close

def Fibo(n, m):
    his = [1, 1]
    months = 2
    while months < n :
        if months < m :
            his.append(his[-1]+his[-2])
        elif months == m:
            his.append(his[-1]+his[-2]-1)
        else:
            sum = 0
            for i in range(months-m, months-1):
                sum += his[i]
            his.append(sum)
        months += 1
    return his[n-1]

print (Fibo(int(set[0]), int(set[1])))