n, tl = map(int, input().split())
c = [0 for i in range(n)]
t = [0 for i in range(n)]
for i in range(n):
    c[i], t[i] = map(int, input().split())
sols = []
for i in range(n):
    if t[i] <= tl:
        sols.append(c[i])
    else:
        continue
if len(sols) == 0:
    print("TLE")
else:
    print(min(sols))
