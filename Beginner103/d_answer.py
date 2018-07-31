n, m = map(int, input().split())
x = [[0, 0] for i in range(m)]
ans = 0
for i in range(m):
    x[i][0], x[i][1] = map(int, input().split())
# for i in range(m):
    # print(x[i])
# print('-'*20)
x = sorted(x, key=lambda y: y[1])
# for i in range(m):
#    print(x[i])
ans += 1
tmp = x[0][1]
for i in range(1, m):
    if x[i][0] < tmp < x[i][1]:
        continue
    else:
        ans += 1
        tmp = x[i][1]
print(ans)
