n, m = map(int, input().split())
if m % n == 0:
    print(m // n)
else:
    gcd = m // n
    for i in range(gcd, 0, -1):
        if m % i == 0:
            j = m // gcd
            if j >= n:
                print(i)
                exit()
