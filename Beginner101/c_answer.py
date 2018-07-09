# グループ分けの数を最初に分かっていれば、いい
n, k = map(int, input().split())
a_tmp = input().split()
a = []
for _ in a_tmp:
    a.append(int(_))
g = 1
while n > (k + (k-1)*(g-1)):
    g += 1
print(g)
