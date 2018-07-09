n, x = map(int, input().split())
m = [[]for i in range(n)]
for i in range(n):
    m[i] = int(input())
nd = n
for i in range(n):
    x -= m[i]
if x >= min(m):
    nd += int(x / min(m))
print(nd)
