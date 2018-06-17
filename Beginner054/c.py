from itertools import permutations

def f(n, m, uu, vv):
    a = [[0] * n for _ in range(n)]
    for u, v in zip(uu, vv):
        #zip関数はリストなどの要素を同時に取得して使うのに使う
        #https://note.nkmk.me/python-zip-usage-for/
        a[u][v] = 1
        a[v][u] = 1
    ##ここの部分でパスが通っているかどうかを入れる。
    ##1と3のパスが通っているならa[1][3]=1かつa[3][1]=1となる
    res = 0
    for p in permutations(range(n)):
        if p[0] != 0:
            break
        #permutationsで作るリストの中身は、1から始まるもの次に2から始まるもの
        #つまり、昇順になっている。要請として1から始まらなきゃいけないので、1から始まらなく
        #なったらリストから抜ける。
        ok = True
        for i in range(n-1):#n-2回ループしたい。
            if a[p[i]][p[i+1]] == 0:#パスが通っていなかったら、抜ける。
                ok = False
                break
        if ok:#パスが通ってたら採用
            res += 1
    return res


n,m = map(int,input().split())
a = []
b = []
#a,bが1セットで、経路を表す。
for i in range(m):
    _a, _b = map(int, input().split())
    _a -= 1
    _b -= 1
    a.append(_a)
    b.append(_b)

print(f(n, m, a, b))
