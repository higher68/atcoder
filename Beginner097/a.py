a, b, c, d = map(int, input().split())
if c-a > d:
    if 0 <= b-a <= d and 0 <= c-b <= d:
        print('Yes')
    else:
        print('No')
elif -d <= c-a <= d:
    print('Yes')
elif c-a < -d:
    if 0 <= a-b <= d and 0 <= b-c <= d:
        print('Yes')
    else:
        print('No')
