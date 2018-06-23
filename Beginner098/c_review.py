n = int(input())
s = input()
west = [0 for _ in range(n)]
if s[0] == 'W':
    west[0] = 1
for _ in range(1, n):
    if s[_] == 'W':
        west[_] = west[_-1] + 1
    else:
        west[_] = west[_-1]
east = [0 for _ in range(n)]
if s[n-1] == 'E':
    east[n-1] = 1
for _ in range(n-2, -1, -1):
    if s[_] == 'E':
        east[_] = east[_+1] + 1
    else:
        east[_] = east[_+1]
ans = [0 for _ in range(n)]
ans[0] = east[1]
for _ in range(1, n-1):
    ans[_] = west[_-1] + east[_+1]
ans[n-1] = west[n-2]

print(min(ans))
