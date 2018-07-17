a = int(input())
b = int(input())
c = int(input())
d = int(input())

ans = 0
if a > b:
    ans += b
else:
    ans += a
if c > d:
    ans += d
else:
    ans += c
print(ans)
