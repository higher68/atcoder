# 提出した方のコードは、1~m/nで全探索していた
# ただ、2つの値の数の合成数として、nが書ける時、
# 小さい方の約数はroot(M)以下である性質を用いたら、
# root(M)で探索すれば良い。ついでにm/aもみてったら、全部の候補で探索できるよね
import math
n, m = map(int, input().split())
root_m = int(math.sqrt(m))
ans = 1
for a in range(1, root_m):
    # print(a, ans)
    if m % a == 0:  # aはmの約数
        b = m // a  # /一つだとfloatになっちゃうので注意
        if a * n <= m:
            ans = max(ans, a)
        if b * n <= m:
            ans = max(ans, b)
print(ans)
