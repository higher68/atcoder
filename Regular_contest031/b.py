import sys
sys.setrecursionlimit(1000000)
##global変数は、関数内で変更するには宣言が必要
##for文内の依存関係がよくわからん
##データを読み出す
map = []
for i in range(10):
    map.append(list(input()))

##startpointを決める

start = False
start_x = 0
start_y = 0
for j in range(10):
    for i in range(10):
        if map[i][j] == 'o':
            start = 'True'
            start_x = i
            start_y = j
            break
    if start: break

o_count0=0
for ch1 in map:
    for ch2 in ch1:
        if ch2 == 'o' :
            o_count0+=1

o_count = 0
o_countx = 0
judge = False
reached = [[False for i in range(10)]for i in range(10)]

def initial_condition():
    global o_count
    global o_countx
    global reached

    for j1 in range(10):
        for i1 in range(10):
            reached[i1][j1] =False
    o_count = 0
    o_countx = o_count0

##DFSの関数
def DFS(x, y):
    global o_count
    global reached

    #print('x,y',x, y)
    if x < 0 or x > 9:
        return
    elif y < 0 or y > 9:
        return
    elif map[x][y] == 'x':
        return
    if reached[x][y]:
        return
    reached[x][y] = True
    o_count += 1

    DFS(x+1, y)
    DFS(x-1, y)
    DFS(x, y+1)
    DFS(x, y-1)

def map_change_p(i, j):
    global map
    map[i][j] = 'o'
def map_change_m(i, j):
    global map
    map[i][j] = 'x'

for j in range(10):
    for i in range(10):
        initial_condition()
        if map[i][j] == 'x':
            map_change_p(i, j)
            o_countx += 1
            DFS(start_x, start_y)
            if o_count == o_countx :
                judge = True
                break
            map_change_m(i, j)
        else:
            o_countx += 1
            DFS(start_x, start_y)
            if o_count == o_countx :
                judge = True
                break
    if judge:break

if judge:
    print('YES')
else:
    print('NO')
