import math


def factoring2(max_input):
    n1 = max_input
    max_input = int(math.fabs(math.sqrt(max_input)))
    pf = []
    data = [1] * (max_input+1)
    m = 2
    n = 0
    while n1 % m == 0:
        n1 //= m
        pf.append(m)
    data[0] = 0
    data[1] = 0
    while 1:
        # print(m)
        if data[m] == 1:
            i = 2 * m
            while i <= max_input:
                data[i] = 0
                i += m
            while n1 % m == 0:
                n1 //= m
                pf.append(m)
            n += 1
            m += 1
        else:
            m += 1
        if n1 == 1:
            return pf
