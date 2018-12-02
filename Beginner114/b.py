s = [int(_) for _ in input().strip()]
diff = 2222222


def abs(x):
    if x < 0:
        return -x
    else:
        return x


for i in range(len(s)-2):
    x = 100 * s[i] + 10 * s[i+1] + s[i+2]
    if abs(x-753) < diff:
        diff = abs(x-753)
    else:
        continue
print(diff)
