n, m, q = map(int, input().split())
ll = [[0, 0] for i in range(m)]
p = [[0, 0] for i in range(m)]
for i in range(m):
    ll[i][0], ll[i][1] = map(int, input().split())
for i in range(q):
    p[i][0], p[i][1] = map(int, input().split())
for i in range(q):
    ans = 0
    for j in range(m):
        if p[i][0] <= ll[j][0] and ll[j][1] <= p[i][1]:
            ans += 1
    print(ans)
