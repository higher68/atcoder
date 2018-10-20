from factoring import factoring
from collections import OrderedDict
from itertools import combinations

n, m = map(int, input().split())

fact_list = list(factoring(m).values())

sol = 1
for val in fact_list:
    sol *= len(list(combinations(range(val+n-1), val)))

print(sol)
