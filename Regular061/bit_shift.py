import itertools

s = '1234'
n = [i for i in s]
ans = 0
#ビットで2の階乗でやる方法
#print(n)
#exit
l = len(s)
#rangeは0引数にした数までの要素をリストを返すっぽい
# +の個数
for i in range(l-1):
    s2 = []
    for j in range(l-1):
        if 1 & i  >> j:
            s2.append(n[j])
            s2.append('+')
        else :
            s2.append(n[j])
    print(s2)
