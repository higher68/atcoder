n, m, x = map(int, input().split())
a_tmp = input().split()
a = []
for _ in a_tmp:
    a.append(int(_))
cost_l = 0
cost_r = 0
j = 0
for i in range(n+1):
    if i < x:
        if i == a[j]:
            cost_l += 1
            j += 1
            if j >= len(a):
                break
    elif x < i:
        if i == a[j]:
            cost_r += 1
            j += 1
            if j >= len(a):
                break
    else:
        continue
print(min(cost_l, cost_r))
