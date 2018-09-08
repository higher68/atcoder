n, x = map(int, input().split())
xl = [int(_) for _ in input().split()]
for i in range(n):
    if x > xl[i]:
        xl[i] = x - xl[i]
    else:
        xl[i] = xl[i] - x


def gcd(a, b):
    if a < b:
        x_a = b
        x_b = a
    else:
        x_a = a
        x_b = b
    while(1):
        if x_a < x_b:
            tmp = x_a
            x_a = x_b
            x_b = tmp
        x_a %= x_b
        if x_a == 0:
            break
    return x_b

    
x_gcd = xl[0]
if n > 1:
    for i in range(1, n):
        x_gcd = gcd(x_gcd, xl[i])
print(x_gcd)
