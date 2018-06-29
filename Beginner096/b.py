a = input().split()
a2 = []
for _ in a:
    a2.append(int(_))
k = int(input())
for i in range(k):
    target = a2.index(max(a2))
    a2[target] *= 2
print(sum(a2))
