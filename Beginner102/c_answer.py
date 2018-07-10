# 実際に点を動かしてみて増減を考えるっていうのが大事なのか？
import math
n = int(input())
a_tmp = input().split()
a_tmp1 = []
for i in range(n):
    a_tmp1.append(int(a_tmp[i])-i-1)
a = sorted(a_tmp1)
if n % 2 == 0:
    x = a[n//2]
else:
    x = a[n//2]
ans = 0
for _ in a:
    ans += math.fabs(_ - x)
print(int(ans))
