n, k = map(int, input().split())
ll = n // k
if k % 2 == 0:
    ans = ll ** 3
    if n >= ll*k + k/2:
        ans += (ll+1)**3
    else:
        ans += ll**3
    print(ans)
else:
    print(ll ** 3)
