from prime_num import prime_num
from collections import OrderedDict


def factoring(n):
    result = prime_num(n)
    print(result)
    loop_len = len(result)
    pf = OrderedDict()
    for i in range(0, loop_len):
        num = 0
        while 1:
            if n % result[i] == 0:
                n /= result[i]
                if num == 0:
                    pf[result[i]] = 1
                else:
                    print(pf[result[i]])
                    pf[result[i]] += 1
                    print(pf[result[i]])
                    num += 1
            else:
                break
        if n == 1:
            return pf


fact = factoring(12)
print(fact)
