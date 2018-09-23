n, m, x, y = map(int, input().split())
l_x = [int(_) for _ in input().split()]
l_y = [int(_) for _ in input().split()]
max_x = max(l_x)
min_y = min(l_y)
if max_x < min_y:
    l_ans = set([i for i in range(max_x+1, min_y+1)])
    l_ans2 = set([i for i in range(x+1, y+1)])
    if l_ans & l_ans2:
        print("No War")
    else:
        print("War")
else:
    print("War")
