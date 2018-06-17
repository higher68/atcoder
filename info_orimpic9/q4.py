from itertools import permutations
n = int(input())#カードの総数
k = int(input())#取り出すカードの総数
a = []
for _ in range(n):
    _a = input()
    a.append(_a)
#文字型の方が制御しやすそう。(桁数を考えなくていいから)
#set()を使えば、集合として制御できるから良さそう.
#数字を連結したリストを生成
pattern_l = permutations(a,k)
pattern_str=[]
for char in pattern_l:
    s = ''
    for _ in char:
        s += _
    pattern_str.append(s)

pattern_sorted = set(pattern_str)#集合型へ
print(len(pattern_sorted))
