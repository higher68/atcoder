from collections import Counter
n = int(input())
v = [int(_) for _ in input().split()]
v1 = []
v2 = []
for i in range(n):
    if i % 2 == 0:
        v1.append(v[i])
    else:
        v2.append(v[i])
v_count = Counter(v)
v1_count = Counter(v1)
v2_count = Counter(v2)
# print("v1_count", v1_count)
# print("v2_count", v2_count)
v1_comm = v1_count.most_common(1)
v2_comm = v2_count.most_common(1)
sols = []
# print("v1_comm", v1_comm)
# print("v2_comm", v2_comm)
if len(v_count) == 1:
    print(n//2)
else:
    key1 = v1_comm[0][1]
    # print("v1_comm[0][0]", v1_comm[0][0])
    # print("v2_comm[0][0]", v2_comm[0][0])
    if v1_comm[0][0] == v2_comm[0][0]:
        # print("hoge")
        v2_comm = v2_count.most_common(2)
        key2 = v2_comm[1][1]
    else:
        key2 = v2_comm[0][1]
    sols.append(n-key1-key2)
    key1 = v2_comm[0][1]
    if v1_comm[0][0] == v2_comm[0][0]:
        v1_comm = v1_count.most_common(2)
        key2 = v1_comm[1][1]
    else:
        key2 = v1_comm[0][1]
    sols.append(n-key1-key2)
    print(min(sols))
