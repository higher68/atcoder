#https://atc001.contest.atcoder.jp/submissions/me#
import sys
sys.setrecursionlimit(1000000)
h, w = map(int, input().split())
c = []

#listで1文字ずつ分割
for i in range(h):
    c.append(list(input()))
#print(c)
judge = False
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            judge = True
            break
    if judge:break
start_x = i
start_y = j
reached = [[False for i in range(w)] for i in range(h)]
#print(c[3][4])
judge = False
#行方向の探査と列方向の探査に注意
for i in range(h):
    for j in range(w):
        if c[i][j] == 'g':
            judge = True
            break
    if judge:break
ans_x = i
ans_y = j
#print(i,j)
#passを書けば何もしない関数を書くことができる。
#print(reached)
#for ch in c:
#    print(len(ch))

def search(x, y):
    #print(x,y)
    if x < 0 or h <= x:
        return
    elif y < 0 or w <= y:
        return
    elif c[x][y] == '#':
        return
    elif reached[x][y]:
        return

    reached[x][y] = True
    search(x + 1, y)
    search(x - 1, y)
    search(x, y + 1)
    search(x, y - 1)
#print(start_x,start_y)
search(start_x, start_y)
#print(reached)
if reached[ans_x][ans_y]:
    print('Yes')
else:
    print('No')
