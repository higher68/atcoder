n = int(input())
s = input()
num = [0 for i in range(n)]
w = [0 for i in range(n)]
if s[0] == 'W':
    w[0] = 1
for i in range(1, n):
    if s[i] == 'W':
        w[i] = (w[i-1] + 1)
    else:
        w[i] = w[i-1]
e = [0 for i in range(n)]
if s[n-1] == 'E':
    e[n-1] = 1
for i in range(2, n+1):
    if s[n-i] == 'E':
        e[n-i] = (e[n-i+1] + 1)
    else:
        e[n-i] = e[n-i+1]
# print(w)
# print(e)
sol = [0 for i in range(n)]
sol[0] = e[0]
sol[n-1] = w[n-2]
for i in range(1, n-1):
    sol[i] = w[i-1] + e[i+1]
print(min(sol))
