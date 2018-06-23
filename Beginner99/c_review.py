n = int(input())
dp = [0 for _ in range(n)]
pat = [1]
i = 0
while 1:
    i += 1
    if 6 ** i < n:
        pat.append(6 ** i)
    else:
        break
i = 0
while 1:
    i += 1
    if 9 ** i < n:
        pat.append(9 ** i)
    else:
        break
dp[0] = 1
for i in range(1, n):
    cand = []
    for _ in pat:
        if i - _ >= 0:
            cand.append(dp[i-_])
    dp[i] = min(cand) + 1

print(dp[n-1])
