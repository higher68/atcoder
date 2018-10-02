from collections import Counter

n = int(input())
v = [int(_) for _ in input().split()]

# 最終的な2値をx, yとしたとき書き換える要素が最小の場合は、
# xは、書き換えが最も少ない数。つまり、もともと最も多い数
# yも同様。
# ただ、xとyがかぶる場合があるので、それに対処。
if len(Counter(v)) > 1:
    v1 = v[0:n+1:2]
    # print(v)
    # print(v1)
    v2 = v[1:n+2:2]
    # print(v2)
    v1_count = Counter(v1)
    v2_count = Counter(v2)

    v1_1st_common = v1_count.most_common(1)   
    v2_1st_common = v2_count.most_common(1)
    sols = []
    # print(v1_1st_common[0][1], v2_1st_common[0][1])
    # v1を基準として多い方を考える場合。
    n1 = v1_1st_common[0][1]
    # v1の1位とv2の1位がかぶる場合
    if v1_1st_common[0][0] == v2_1st_common[0][0]:
        if len(v2_count) >= 2:
            v2_2nd_common = v2_count.most_common(2)
            n2 = v2_2nd_common[1][1]
        else:
            print(n//2)
    else:
        n2 = v2_1st_common[0][1]
    sols.append(n-n1-n2)

    # v2を基準として多い方を考える場合。
    n2 = v2_1st_common[0][1]
    # v1の1位とv2の1位がかぶる場合
    if v1_1st_common[0][0] == v2_1st_common[0][0]:
         if len(v1_count) >= 2:
            v1_2nd_common = v1_count.most_common(2)
            n1 = v1_2nd_common[1][1]
         else:
            print(n//2)
    else:
        n1 = v1_1st_common[0][1]
    sols.append(n-n1-n2)
    print(min(sols))
else:
    print(n//2)
