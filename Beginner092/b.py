import math
n = int(input())
d, x = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
count_day = [0 for i in range(n)]
for i in range(n):
    count_day[i] = math.ceil(d / a[i])
ans = x + sum(count_day)
print(ans)
