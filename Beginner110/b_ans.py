# Xとx_iを同一視する。
n, m, x, y = map(int, input().split())
x_list = [int(_) for _ in input().split()]
x_list.append(x)
y_list = [int(_) for _ in input().split()]
y_list.append(y)
x_max = max(x_list)
y_min = min(y_list)
if x_max < y_min:
    print("No War")
else:
    print("War")
