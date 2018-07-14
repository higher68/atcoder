t = int(input())
a = [0 for i in range(t)]
b = [0 for i in range(t)]
c = [0 for i in range(t)]
d = [0 for i in range(t)]
for i in range(t):
    a[i], b[i], c[i], d[i] = map(int, input().split())
for i in range(t):
    count = 0
    m_set = set()
    if a[i] - b[i] > c[i]:
        m_set = m_set | set([a[i] - b[i]*j for j in range((a[i]-c[i]) // b[i])])
        tmp = a[i] - b[i] * ((a[i]-c[i]) // b[i] - 1)
    else:
        tmp = a[i]
    while count < 10000:
        m_set.add(tmp)
        if tmp < b[i]:
            print('No')
            break
        tmp -= b[i]
        if tmp <= c[i]:
            tmp += d[i]
            if tmp - b[i] > c[i]:
                m_set = m_set | set([tmp - b[i]*j for j in range((tmp-c[i]) // b[i])])
                tmp = tmp - b[i] * ((tmp-c[i]) // b[i] - 1)
        s1 = set()
        s1.add(tmp)
        if s1.issubset(m_set):
            print('Yes')
            break
        # print(tmp)
        count += 1
    if count == 10000:
        print('Yes')
