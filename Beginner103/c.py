n = int(input())
a = [0 for i in range(n)]
a_tmp = input().split()
for i in range(n):
    a[i] = int(a_tmp[i])
ans = 0
for i in range(n):
    ans += a[i] -1
print(ans)
