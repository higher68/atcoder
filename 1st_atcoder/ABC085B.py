###入力
n = int(input())
##d[]=0みたいな宣言はできない？
d = []
for i in range(n):
    d.append(int(input()))
hight = 1
wh = 0
max = 0
for i in range(len(d)):
    if d[i] > max:
        max = d[i]
        wh = i
    else:
        pass
del d[wh]
#builtin_function_or_method' object is unsubscriptable　len[]だと、予約文字を使ってしまっている。
while len(d):
    max_tmp = 0
    for i in range(len(d)):
        if d[i] > max_tmp:
            max_tmp = d[i]
            wh = i
        else:
            pass
    if max > max_tmp:
        max = max_tmp
        hight += 1
    else:
        pass
    del d[wh]


##もうちょっと頭のいいやり方ある気がするんだけどなあ。。。
print(hight)
