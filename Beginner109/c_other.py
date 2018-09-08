# 本番環境はpython3.4.3環境であることに注意。
# 上記環境では、"math"でなく"fraction「s」"にgcdが存在するので注意
import fractions
n, x = map(int, input().split())
xl = [int(_) for _ in input().split()]
for i in range(n):
    if x > xl[i]:
        xl[i] = x - xl[i]
    else:
        xl[i] = xl[i] - x

x_gcd = xl[0]
if n > 1:
    for i in range(1, n):
        x_gcd = fractions.gcd(x_gcd, xl[i])
print(x_gcd)
