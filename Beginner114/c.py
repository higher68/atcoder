from collections import Counter
import sys
sys.setrecursionlimit(10000)

s_n = input()
n = int(s_n)
ans = 0
add_list = ["3", "5", "7"]


def rec(now, i):
    # print(now, i)
    global ans
    coun = len(Counter(now))
    if coun > 2:
        # print("coun", coun)
        if int(now) <= n:
            # print("hoge")
            ans += 1
        else:
            return 0
    if i > -1:
        for j in range(3):
            rec(now + add_list[j], i-1)
    else:
        return 0


rec("", len(s_n)-1)
print(ans)
