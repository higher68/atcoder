from prime_num import prime_num
from collections import OrderedDict
from itertools import combinations
import math
# combinationsは、第一引数はリスト
# 第二引数を入れると組み合わせになる
n, m = map(int, input().split())
# print(factoring(m).items())
# python3ではiteritemsはitemsに変わってる。
# 素因数分解がO(sqrt(N))でいい理由はメモ〜素因数分解をする時、試し割りをするのがsqrt(N)までで良いことの証明〜を参照

try_prime_list = prime_num(int(math.fabs(n)))
prime_dict = OrderedDict()
for_prime_max = 1
for i in try_prime_list:
    count_1st = True
    while m % i == 0:
        for_prime_max *= i
        if count_1st:
            prime_dict[i] = 0
            count_1st = False
        m //= i
        prime_dict[i] += 1
    if m == 1:
        break

if m // for_prime_max != 1:
    prime_dict[m // for_prime_max] = 1

sol = 1
for key in prime_dict:
    sol *= len(list(combinations(range(prime_dict[key]+n-1), prime_dict[key])))

print(sol)
