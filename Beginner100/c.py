n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a0 = []
for _ in range(n):
    i = 0
    x = a[_]
    while 1:
        if x % 2 == 0:
            x = x / 2
            i += 1
        else:
            break
    a0.append(i)
print(sum(a0))

i = 0
amax = 1000000000
_ = 0
while 1:
    if max(a0) == 0:
        break
    elif max(a) > amax:
        break
    i += 1
    while 1:
        if _ >= n:
            _ = 0
            break
        if a0[_] > 0:
            a0[_] -= 1
            if _ >= n:
                _ = 0
            break
        _ += 1
    # print(a0)
    for _1 in range(n):
        if _1 != _:
            if a[_1] * 3 > amax:
                if a0[_1] > 0:
                    a[_1] /= 2
                    a0[_1] -= 1
                else:
                    break
            else:
                a[_1] *= 3
        else:
            a[_1] /= 2

print(i)
