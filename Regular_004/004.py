import math
#pythoの2次元配列はi[][]みたいな感じ
##debug用のprint残したまま提出しない。。。
n = int(input())
x = []
y = []
for i in range(n):
    t_x, t_y = map(int, input().split())
    x.append(t_x)
    y.append(t_y)
l = [[0 for i in range(n)] for j in range(n)]
#print('-------------------')
##Tex使いすぎたな笑乗算は、^でなく**
for i in range(n):
    for j in range(n):
        #print((x[i]-x[j])**2, (y[i]-y[j])**2)
        l[i][j] = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)

l_max = l[0][0]
for v_1 in l:
    for v_2 in v_1:
        if v_2 > l_max:
            l_max = v_2


print(l_max)
#改行入れ忘れマンつらみ
