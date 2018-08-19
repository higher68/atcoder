n, m, q = map(int, input().split())
ll = [[0, 0] for i in range(m)]
p = [[0, 0] for i in range(m)]
for i in range(m):
    ll[i][0], ll[i][1] = map(int, input().split())
for i in range(q):
    p[i][0], p[i][1] = map(int, input().split())
ll = sorted(ll, key=lambda x: x[0])
for i in range(q):
    ans = 0
    if max(ll[:][0]) < p[i][0]:
        print(ans)
        continue
    else:
        if p[i][1] < min(ll[:][1]):
            print(ans)
            continue
        else:
            for j in range(m):
                if p[i][0] > ll[j][0]:
                    continue
                if ll[j][1] > p[i][1]:
                    continue
                ans += 1
    print(ans)
