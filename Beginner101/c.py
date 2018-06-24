n, k = map(int, input().split())
a_tmp = input().split()
a = [[] for i in range(n)]
for i in range(n):
    a[i] = int(a_tmp[i])
a1 = a.index(1)
sol = 0
if k < n//2:
    a_left = a1
    a_right = len(a)-1-a1
    if a_left % (k-1) == 0:
        sol += int(a_left / (k-1))
    else:
        sol += int(a_left / (k-1)) + 1
    if a_right % (k-1) == 0:
        sol += int(a_right / (k-1))
    else:
        sol += int(a_right / (k-1)) + 1
    print(sol)
elif n > k >= n//2:
    if n % 2 == 0:
        print(2)
    else:
        print(n // 2)
else:
    print(1)
