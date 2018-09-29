from collections import Counter
n = int(input())
v_tmp = input().split()
v = [int(_) for _ in v_tmp]
v_count = Counter(v_tmp)
# print(v_count)
if len(v_count) == 1:
    print(n//2)
else:
    # print("hoge")
    v_keys = list(v_count.keys())
    tmps = []
    # print(v_keys)
    for _ in v_keys:
        for _2 in v_keys:
            tmp = []
            # print(_, _2)
            if _ == _2:
                continue
            else:
                for i in range(n):
                    if i % 2 == 0:
                        tmp.append(_)
                    else:
                        tmp.append(_2)
            # print("tmp", tmp)
            if tmp == []:
                continue
            else:
                tmps.append(tmp)
    sols = []
    for _ in tmps:
        sol_tmp = 0
        for i in range(n):
            if _[i] != v_tmp[i]:
                sol_tmp += 1
        sols.append(sol_tmp)
    print(min(sols))
