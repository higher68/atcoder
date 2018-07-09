import math
n = int(input())
a_tmp = input().split()
a = []
for i in range(n):
    a.append(int(a_tmp[i]))
a1 = []
for i in range(n):
    a1.append(a[i]-1-i)
print(a1)
b_max = max(a1)
b_min = min(a1)
sadness = []
for b in range(b_min, b_max+1):
    print(b)
    abs = [math.fabs(a1[i]-b) for i in range(n)]
    sadness.append(int(sum(abs)))
print('min', min(sadness))
print(sadness)
