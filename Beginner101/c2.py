n, k = map(int, input().split())
a_tmp = input().split()
a = [[] for i in range(n)]
for i in range(n):
    a[i] = int(a_tmp[i])
a1 = a.index(1)
if n != k:
    if a1 < k or n-1-k < a1:
        if n-k+1 % k == 0:
            sol = int((n-k+1) / k) + 1
        else:
            sol = int((n-k+1) / k) + 2
        print(int(sol))
    else:
        sol = 0
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
else:
    print(1)
