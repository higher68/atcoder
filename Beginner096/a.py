a, b = map(int, input().split())
sol = 0
for i in range(1, a+1):
    if i == a:
        if b >= a:
            sol += 1
    else:
        sol += 1
print(sol)
