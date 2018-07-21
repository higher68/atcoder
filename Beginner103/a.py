import math
a_tmp = input().split()
a = []
for i in range(3):
    a.append(int(a_tmp[i]))
cost = [0 for i in range(3)]
for i in range(3):
    for j in range(3):
        cost[i] = cost[i] + math.fabs(a[i] - a[j])
print(int(min(cost)))
