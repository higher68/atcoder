# 5000**2、5000**3
# 5文字以下だよ。辛いよ。はえ〜〜〜クリア
# 最初に計算量を見積もる癖をつける必要があるかもなあ
s = input()
k = int(input())
sbst = set()
for i in range(1, k+1):
    for j in range(len(s)-i+1):
        sbst.add(s[j:j+i])
sbstl = sorted(list(sbst))
print(sbstl[k-1])
