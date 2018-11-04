import math
n = int(input())
t, a = map(int, input().split())
h = [int(_) for _ in input().split()]

t_list = []
for i in range(n):
    t_list.append(math.fabs(t-h[i]*0.006 - a))

sol = min(t_list)
for i in range(n):
    if t_list[i] == sol:
        print(i+1)
        exit()
