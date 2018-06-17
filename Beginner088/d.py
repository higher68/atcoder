from collections import deque
h, w =map(int, input().split())
s = [input() for i in range(h)]
s_x, s_y = 0, 0
##ある場所を塗る。その上でBFS。最大値を求める。
#最短経路で辿り着く時、塗りつぶす手は最大になる。
#最短経路の時は、通るますが考えうる中で一番少ないからねえ。そりゃそうか。
max = 0
c = [[0] * w for i in range(h)]
#cを定義する時は、横に並べてからそれを縦に並べる。つまり、列数を指定してから、その外で
#行数を指定する。ただ、要素にアクセスするときは、c[行番号][列番号]
#外側ほど、左側の要素になる？
def BFS():
    q = deque()
    q.append((s_x, s_y))

    while len(q) > 0:
        y, x = q.popleft()
        if y == h - 1 and x == w - 1:
            return c[y][x]
        if x < w - 1:
            if s[y][x+1] == '.' and c[y][x+1] == 0:
                q.append((y, x+1))
                c[y][x+1] = c[y][x] + 1
        if x > 0:
            if s[y][x-1] == '.' and c[y][x-1] == 0:
                q.append((y, x-1))
                c[y][x-1] = c[y][x] + 1
        if y < h - 1:
            if s[y+1][x] == '.' and c[y+1][x] == 0:
                q.append((y+1, x))
                c[y+1][x] = c[y][x] + 1
        if y > 0:
            if s[y-1][x] == '.' and c[y-1][x] == 0:
                q.append((y-1, x))
                c[y-1][x] = c[y][x] + 1

    return(-1)

area = h*w
blunk_num_origin = 0
for ch1 in s:
    for ch2 in ch1:
        if ch2 == '#':
            blunk_num_origin += 1

min_grid = BFS()
if min_grid == -1:
    print(min_grid)
else:
    sol = area-blunk_num_origin-2-(min_grid-1)
    #print(area,min_grid,blunk_num_origin)
    print(sol)
