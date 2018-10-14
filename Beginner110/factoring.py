import prime_num


def factoring(n):
    i = 0
    j = 0
    result = prime_num(n)
    loop_len = len(result)
    pf = {}
    for i in range(0, loop_len):
        num = 0
        while 1:
            if n % result[i] == 0:
                if num == 0:
                    pf[result[i]] = 1
                else:
                    pf[result[i]] += 1
