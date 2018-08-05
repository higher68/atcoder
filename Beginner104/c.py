d, g = map(int, input().split())
p = [[0,0] for i in range(d)]
for i in range(d):
    p[i][0], p[i][1] = map(int, input().split())
ans = 0
sum = 0
i = d
j = 0
extra_ans = [p[i][0] * (i+1) * 100 + p[i][1] for i in range(d)]
while sum < g:
    j += 1
    ans += 1
    sum += i * 100
    if j == p[i-1][0]:
        sum += p[i-1][1]
        i -= 1
        j = 0
    if sum + extra_ans[i-2] >= g :
        tmp = ans + p[i-2][0]
if tmp < ans:
    ans = tmp
for i in range(d):
    if p[i][0] * (i+1) * 100 + p[i][1] >= g and p[i][0] < ans:
        ans = p[i][0]
print(ans)
