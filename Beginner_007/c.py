#https://beta.atcoder.jp/contests/abc007/tasks/abc007_3
##コード自体はあってる。だが、再帰的呼び出しだとこの問題では時間がかかりすぎる。
import sys
sys.setrecursionlimit(1000000)
r,c = map(int,input().split())##rは行数、cは列数

sy,sx = map(int,input().split())#start地点の座標
gy,gx = map(int,input().split())#goal地点の座標
sx -= 1
sy -= 1
gx -= 1
gy -= 1
ch =[]
for i in range(r):
    ch.append(list(input()))

#print(ch)
#print(c, r)
##listは内側が列方向、外側が行方向
trouble = [[0 for i in range(c)] for i in range(r)]
counted = [[False for i in range(c)] for i in range(r)]
n_s = 0
#for j in range(c):
#    for i in range(r):
#        if ch[i][j] == '.':
#            n_s += 1
reach_count=0
#print(c, r)
##ch[i][j]とやった時、i方向は、行番号、j方向は列番号
##今回、rは行数、cは列数
#for i in range(r):
#    for j in range(c):
#        print(i,j,ch[i][j])
#ix =0
def BFS(x, y, z):
    global trouble
    global ix
    global counted
    #ix += 1
    #if ix ==8: exit()
    #print(x,y,z, ch[y][x], counted[y][x])
    if sx == gx and sy == gy:
        #print('hoge1')
        return
    if ch[y][x]  == '#':
        #print('hoge2')
        return
    elif x < 0 or c-1 < x:
        #print('hoge3')
        return
    elif y < 0 or r-1 < y:
        #print('hoge4')
        return
    if counted[y][x]:
        if z != 0 and z < trouble[y][x]:
            trouble[y][x] = z + 1
        else:
            #print('hoge5')
            return
    else:
        if x == sx and y == sy:
            trouble[y][x] == 0
        else:
            trouble[y][x] = z + 1
    #print('hoge6')

    counted[y][x] = True

    #print(counted[y][x])

    #print(x, y, 'x+1')
    BFS(x + 1, y, trouble[y][x])
    #print(x, y, 'x-1')
    BFS(x - 1, y, trouble[y][x])
    #print(x, y, 'y+1')
    BFS(x, y + 1, trouble[y][x])
    #print(x, y, 'y-1')
    BFS(x, y - 1, trouble[y][x])



BFS(sx, sy, trouble[sx][sy])

#print('hoge-ge')
#print(trouble)

print(trouble[gy][gx])
