n = int(input())
s = []
for i in range(n):
    s.append(input())
m = int(input())
t = []
for i in range(m):
    t.append(input())
ans = []
for _ in s:
    ans.append(s.count(_)-t.count(_))
if max(ans) >= 0:
    print(max(ans))
else:
    print(0)
