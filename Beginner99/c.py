n = int(input())
ans = 0
i = 1
nx = n
while 1:
    mon = 9 ** i
    n1 = nx - mon
    print('9', n1)
    if n1 < 0:
        print('hoge1', nx)
        if i > 1:
            print('hoge3', nx)
            nx -= 9 ** (i-1)
            # 教訓：べきに数字を書くときはカッコをつけること。
            print('hoge4', nx)
            ans += i-1
        break
    i += 1
print('ans', ans, nx)
i = 1
while 1:
    mon = 9 ** i
    n1 = nx - mon
    print('6', n1)
    if n1 < 0:
        print('hoge2', nx)
        if i > 1:
            nx -= 6 ** i-1
            ans += i-1
        break
    i += 1
print('ans', ans, nx)
ans += nx

print(ans)
