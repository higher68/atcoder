d, n = map(int, input().split())
sol = n * 100 ** d
if n == 100:
    if d == 0:
        print(101)
    elif d == 1:
        print(10100)
    elif d == 2:
        print(1010000)
else:
    print(sol)
