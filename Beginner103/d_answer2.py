n, m = map(int, input().split())
# stdin.readlines?
x = [[0, 0] for i in range(m)]
for i in range(m):
    x[i][0], x[i][1] = map(int, input().split())
x = sorted(x, key=lambda y: y[0])
ans = 1
mx = max([x[i][0] for i in range(m)])
while len(x) > 0:
    for i in range(len(x)-1, -1, -1):
        if mx < x[i][1]:
            x.pop(i)
            break
        else:
            mx = x[i][0]
            ans += 1
            break
print(ans)
