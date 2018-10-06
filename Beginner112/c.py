import math
n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
h = [0 for i in range(n)]
judge = False
for i in range(n):
    x[i], y[i], h[i] = map(int, input().split())
for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, n):
            if h[k] != 0:
                true_h = h[k] + int(math.fabs(x[k]-i)) + int(math.fabs(y[k]-j))
                break
        judge = True
        for k in range(n):
            dum_h = max(true_h-int(math.fabs(x[k]-i)) - int(math.fabs(y[k]-j)), 0)
            if h[k] != dum_h:
                judge = False
                break
        # print(k)
        if judge is True:
            break
    if judge is True:
        break

print("{} {} {}".format(i, j, true_h))
