n = int(input())

if n == 0:
    print('0')
else:
    ans = []
    x = n
    while x != 1:
        if x % -2 == 0:
            ans.append('0')
            x //= -2
        else:
            ans.append('1')
            x //= -2
            x += 1
    ans.append('1')
    t_ans = ''
    for i in range(len(ans)-1, -1, -1):
        t_ans += ans[i]
    print(t_ans)
