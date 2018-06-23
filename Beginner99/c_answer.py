# DPの基本形。
# DPとは動的計画法のこと
# DP漸化式を立てて問題を解く。どんな式を立てるかが問題(状態の撮り方)
# 一番簡単なもの・・・問題の答えを状態とする。dp[N]の満たす漸化式を求めに行く。

# dp[1]・・・・dn[N-1]を知ってるとして、dp[N]を求めたい。
# dp。場合分けするといい。まずは1円玉
# 10円持っている時に、例えば1円をとったら、9円。
# そこから最小の取り方を求めるには、9円の時の取り出す枚数最小の取り方を求めればいい。
# つまり1円を取り出すとわかっている時、f(10) = min(f(9))+1である。
# ここで、取り出し方は1,6,6^2,・・・6^なんとか、9^1,9^2,・・・9^なんとか
# f(x)を取り出す時の最小の手数は、上の取り出し方の候補をxから引いたもののうち、最小のもの+1
# したがって、x=1~nで、各場合の最小の手数を求めれば、任意の場合の手数がわかる。
# x円持っている時の最小の取り方を
# https://31536000.hatenablog.com/entry/2018/06/10/231720
n = int(input())
dp = [0 for i in range(n)]
a = [1]
i = 1
_ = 6
while _ <= n:
    a.append(_)
    i += 1
    _ = 6 ** i
i = 1
_ = 9
while _ <= n:
    a.append(_)
    i += 1
    _ = 9 ** i
len_a = len(a)
for i in range(n):
    # print('i', i)
    target = []
    for j in range(len_a):
        if i + 1 >= a[j]:
            target.append(dp[i - a[j]])
        # print('target', target)
    dp[i] = min(target) + 1
# for i in range(len(dp)):
    # print('dp', i+1, dp[i])
print(dp[n-1])
