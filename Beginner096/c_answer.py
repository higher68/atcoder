
# 条件分けして、数学的帰納法で片方の条件を検証。
# 棄却されてない方で全ての事象を調べる。
# 周囲を調べる時は、先にキャンパスを上下左右に1マス拡張しておく。
# 例外処理がなくなっていいね。
h, w = map(int, input().split())
s = [[] for i in range(h+2)]
s[0] = '.'*(w+2)
for i in range(1, h+1):
    s[i] = '.' + input() + '.'
s[h+1] = '.'*(w+2)
s2 = [[False for j in range(w)] for i in range(h)]
# for j in range(h+2):
#     print(s[j])
# マスを一つ黒く塗ろうとすると、それに隣接したものも塗られてしまう。
# しかも最初は白で塗られている
# なので、黒マスの周囲には必ず1つは黒マスがある。
# #が#と隣接していない場合、目標は達成できない。
# なぜなら、2個数一緒に塗る必要があるため。
# その上で、#が#と隣接している時、
# m個数のマスがぬれたとして、残りの1マスを塗るときに、
# すでに使ったマスを使える。なので、m+1の時塗れる。
# #が2このときは自明なので、帰納法より、m個数の時、濡れる。
# 以上から、1つも隣接していない黒マスがあるかどうかを調べれば良い。
judge = True
for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == "#":
            if [s[i+1][j], s[i-1][j], s[i][j-1], s[i][j+1]] \
            == ['.', '.', '.', '.']:
                judge = False

        else:
            continue
        if not judge:
            break
    if not judge:
        break
if judge:
    print('Yes')
else:
    print('No')
