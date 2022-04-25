#LGIS

file = open("/Users/useung-yeon/Desktop/Bioinfo/Rosalind/rosalind_lgis.txt", "r")
s=file.read().split()
x = int(s[0])
arr = []
for i in range(1, len(s)):
    arr.append(int(s[i]))
file.close()

in_dp = [0 for i in range(x)]
de_dp = [0 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            in_dp[i] = max(in_dp[i], in_dp[j]+1)
        if arr[i] < arr[j]:
            de_dp[i] = max(de_dp[i], de_dp[j]+1)
max_in_dp, max_de_dp = max(in_dp), max(de_dp)

max_in_idx = in_dp.index(max_in_dp)
max_de_idx = de_dp.index(max_de_dp)


lis = []
lds = []
while max_in_idx >= 0:
    if in_dp[max_in_idx] == max_in_dp:
        lis.append(arr[max_in_idx])
        max_in_dp -= 1
    max_in_idx -= 1
lis.reverse()
print (*lis)

while max_de_idx >= 0:
    if de_dp[max_de_idx] == max_de_dp:
        lds.append(arr[max_de_idx])
        max_de_dp -= 1
    max_de_idx -= 1
lds.reverse()
print (*lds)