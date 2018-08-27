# あらかじめ全ての区間における答えを求めておく
# 累積和が使える。
# 2次元累積和に関しては、下記のサイトを参照。
# https://paiza.hatenablog.com/entry/2014/05/28/もし女子大生プログラマに『アルゴリズム』を図
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
# for i in range(m):
#     print(ll[i])
# for i in range(q):
#     print(p[i])
sum = [[0 for i in range(n)] for i in range(n)]
# sum上でlをy成分＝行、rをx成分=列とする。
# 各区間の値を取り込み
for j in range(m):
    x = ll[j][0]-1
    y = ll[j][1]-1
    sum[y][x] += 1
# 2次元累積和の計算
# for j in range(n):
#     print(sum[j])
# print('-'*30)
for i in range(n):
    for j in range(1, n):
        sum[i][j] += sum[i][j-1]
for i in range(n):
    for j in range(1, n):
        sum[j][i] += sum[j-1][i]
# ans = [[0 for i in range(n)] for i in range(n)]
# for i in range(n):
#    for j in range(i, n):
#        for i2 in range(i, j+1):
#            for j2 in range(i, j+1):
#                ans[i][j] += sum[j2][i2]
# for j in range(n):
#     print(sum[j])


for i in range(q):
    x = p[i][0]-1
    y = p[i][1]-1
    if x != 0:
        print(sum[y][y] - sum[y][x-1] - sum[x-1][y]+sum[x-1][x-1])
    else:
        print(sum[y][y])
