from factoring2 import factoring2
from collections import Counter
from itertools import combinations
# combinationsは、第一引数はリスト
# 第二引数を入れると組み合わせになる
n, m = map(int, input().split())
# print(factoring(m).items())
# python3ではiteritemsはitemsに変わってる。
dic = Counter(factoring2(m))
fact_list = list(dic.values())

sol = 1
for val in fact_list:
    sol *= len(list(combinations(range(val+n-1), val)))

print(sol)
