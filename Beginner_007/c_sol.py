#https://beta.atcoder.jp/contests/abc007/tasks/abc007_3
##コード自体はあってる。だが、再帰的呼び出しだとこの問題では時間がかかりすぎる。
from collections import deque
##https://www.lifewithpython.com/2014/06/collectionsdeque.html
##キュー・スタックを効率的に行えるようになるライブラリ
##BFSは、ある層に関して探索し、その層が終わったら次を行うもの
##DFSは深い方へ進めるだけ進み、進めなくなったら戻ってくる。
##BFSの概念的に、今回の層は、低層から調べているので、かぶることはない
import sys
sys.setrecursionlimit(1000000)
r,c = map(int,input().split())##rは行数、cは列数
sy,sx = map(int,input().split())#start地点の座標
gy,gx = map(int,input().split())#goal地点の座標
ch =[input() for i in range(r)]
trouble = [[0 for i in range(c)] for i in range(r)]

q = deque()
#print(sy,sx)
q.append((sy-1, sx-1))##実際のリストの配列番号に置き換えてる。
#i=0
while len(q) > 0:
    #print(q,'hoge1')
    y, x = q.popleft()##この場合、代入してから、popleftが適用されているらしい。
    ##さらに、キューの先頭がy,xに格納されているらしい。
    #i += 1
    #print(y,x)
    #print(q,'hoge2')
    #if i == 6:exit()
    #popleft():deque の左側から要素をひとつ削除し、その要素を返します。
    #要素がひとつも存在しない場合は IndexError を発生させます。
    #先頭に関して、可能性を4パターン考える。その上で、さらに可能性が考えられそうだったら、
    #追加して保留。次のループに行って、溜まってるタスクを処理
    #それを繰り返す。問題は、2パターンの辿りつき方がある時にこれで全てのパターンを
    #もうらできるのかがよくわからん
    if y == gy-1 and x == gx-1:
        print(trouble[gy-1][gx-1])
        break
    if x < c-1:
        if ch[y][x+1] == '.' and trouble[y][x+1] == 0:
            q.append((y, x+1))
            ##appendは右側に追加
            trouble[y][x+1] = trouble[y][x] + 1
    if x > 0:
        if ch[y][x-1] == '.' and trouble[y][x-1] == 0:
            q.append((y, x-1))
            trouble[y][x-1] = trouble[y][x] + 1
    if y < r-1:
        if ch[y+1][x] == '.' and trouble[y+1][x] == 0:
            q.append((y+1, x))
            trouble[y+1][x] = trouble[y][x] + 1
    if y > 0:
        if ch[y-1][x] == '.' and trouble[y-1][x] == 0:
            q.append((y-1, x))
            trouble[y-1][x] = trouble[y][x] + 1

#print(ch)
#print(c, r)
##listは内側が列方向、外側が行方向
