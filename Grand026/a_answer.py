# 小さい例を集めるパターン
n = int(input())
a_tmp = input().split()
a = []
for _ in a_tmp:
    a.append(int(_))
ans = 0
same = 1
tmp = a[0]
for i in range(1, n):
    # print(i, same, ans)
    if tmp != a[i]:
        ans += same // 2
        same = 1
        tmp = a[i]
    else:
        same += 1
ans += same // 2
print(ans)
