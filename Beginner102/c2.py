import math
n = int(input())
a_tmp = input().split()
a = []
for i in range(n):
    a.append(int(a_tmp[i]))
a1 = []
for i in range(n):
    a1.append(a[i]-1-i)
b_max = max(a)
b_min = min(a)
sadness = []
b_mean = (b_max-b_min)//2
print(b_mean, b_max, b_min)
for b in range(b_mean-1, b_mean+1):
    abs = [math.fabs(a[i]-b-i-1) for i in range(n)]
    sadness.append(int(sum(abs)))
print(sadness)
