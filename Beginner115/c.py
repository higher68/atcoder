n, k = map(int, input().split())
h = []

for i in range(n):
    h.append(int(input()))
min = 10 ** 10
#  print(h)
h = sorted(h)
#  print(h)
for i in range(n-k+1):
    #  print(h[i:i+k-1])
    div = h[i+k-1] - h[i]
    if div < min:
        min = div
    if min == 0:
        print(min)
        exit()
print(min)
