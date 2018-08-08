# 周囲を調べる時は、先にキャンパスを上下左右に1マス拡張しておく。
# 例外処理がなくなっていいね。
h, w = map(int, input().split())
s = [[] for i in range(h+2)]
s[0] = '.'*(w+2)
for i in range(1, h+1):
    s[i] = '.' + input() + '.'
s[h+1] = '.'*(w+2)
s2 = [[False for j in range(w)] for i in range(h)]
for j in range(h+2):
    print(s[j])
