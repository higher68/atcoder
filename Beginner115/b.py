n = int(input())
p = []
sum = 0
for i in range(n):
    p.append(int(input()))
mp = max(p)
nesage = False
for i in range(n):
    if p[i] == mp and not nesage:
        sum += int(p[i]/2)
        nesage = True
    else:
        sum += p[i]
print(sum)
