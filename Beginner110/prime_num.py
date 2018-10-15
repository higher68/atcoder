def prime_num(max_input):
    data = [1] * (max_input+1)
    result = [0] * (max_input+1)
    m = 2
    n = 0
    result[n] = m
    data[0] = 0
    data[1] = 0
    while 1:
        # print(m)
        if data[m] == 1:
            i = 2 * m
            while i <= max_input:
                data[i] = 0
                i += m
            result[n] = m
            n += 1
            m += 1
        else:
            m += 1
        if m > max_input:
            return result[:n]


# print(prime_num(12))
