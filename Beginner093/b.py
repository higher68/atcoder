a, b, k = map(int, input().split())
x = []
for i in range(a, b+1):
    x.append(i)
lx = len(x)
if k < lx//2:
    for i in range(k):
        print(x[i])
    for i in range(lx-k, lx):
        print(x[i])
else:
    for i in x:
        print(i)
