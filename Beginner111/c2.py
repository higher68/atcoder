from collections import Counter
n = int(input())
v_tmp = input().split()
v = [int(_) for _ in v_tmp]
v_count = Counter(v_tmp)
v2_tmp = []
for i in range(0, n-1,  2):
    v2_tmp.append((v[i], v[i+1]))
v2_count = Counter(v2_tmp)
# print(v_count)
if len(v_count) == 1:
    print(n//2)
elif len(v_count) == n:
    print(n-2)
else:
    val_mx = max(list(v2_count.values()))
    v2_list = v2_count.most_common(1)[0]
    sum = 0
    # print(v2_list[0][0])
    # print(v2_list[0][1])
    for i in range(n):
        if i % 2 == 0 and v[i] == v2_list[0][0]:
            sum += 1
        elif i % 2 == 1 and v[i] == v2_list[0][1]:
            sum += 1
    print(n-val_mx*2-(sum-val_mx*2))
