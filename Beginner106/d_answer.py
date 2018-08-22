# あらかじめ全ての区間における答えを求めておく
# 累積和が使える。
# p,qの値に関しての2次元座標系で考えると、値が存在するマスは限られてる
#
#
n, m, q = map(int, input().split())
ll = [[0, 0] for i in range(m)]
p = [[0, 0] for i in range(q)]
for i in range(m):
    ll[i][0], ll[i][1] = map(int, input().split())
for i in range(q):
    p[i][0], p[i][1] = map(int, input().split())
for i in range(m):
    print(ll[i])
for i in range(q):
    print(p[i])
sum = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if ll[j][0] == i+1 and ll[j][1] == i+1:
            sum[i][i] += 1
    for j in range(i+1, n):
        sum[j][i] += sum[j-1][i]
        for k in range(m):
            if ll[k][0] == i+1 and ll[k][1] == j+1:
                print(i, j)
                sum[j][i] += 1
            else:
                continue
for i in range(n):
    print(sum[i])
# exit()
for i in range(q):
    print(sum[p[i][1]-1][p[i][0]-1])
