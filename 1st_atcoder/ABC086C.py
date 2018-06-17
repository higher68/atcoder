##2d平面
##t0, x,y=0,0
##ti = xi,yi
#1<i<N
#いけたー
n = int(input())
ti =[]
xi =[]
yi = []
for i in range(n):
    t_t, x_t, y_t = map(int, input().split())
    ti.append(t_t)
    xi.append(x_t)
    yi.append(y_t)

can = True
t=0
x=0
y=0
##奇数だと戻ってこれないか。
for i in range(n):
    dt = ti[i] - t
    dx = xi[i] - x
    dy = yi[i] - y
    if dt >= dx + dy and (dt-dx-dy)%2 == 0:
        t = ti[i]
        x = xi[i]
        y = yi[i]
    else :
        can = False
        break

if can:
    print('Yes')
else:
    print('No')
