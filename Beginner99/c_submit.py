n = int(input())


def judge(nx):
    i = 1
    while 1:
        mon = 9 ** i
        n1 = nx - mon
        if n1 < 0:
            # print(n1, mon, nx, i)
            if i > 1:
                ans1 = 9 ** (i-1)
                break
        i += 1
    i = 1
    while 1:
        mon = 6 ** i
        n1 = nx - mon
        if n1 < 0:
            # print(n1, mon, nx, i)
            if i > 1:
                ans2 = 6 ** (i-1)
                break
        i += 1
    # print(ans1, ans2)
    if ans1 > ans2:
        return ans1
    else:
        return ans2


ans = 0
nx = n
while nx >= 18:
    # print('-------')
    # print(nx)
    d = judge(nx)
    # print(d)
    # print('-------')
    nx -= d
    ans += 1

# print(nx)
ans += nx

print(ans)
