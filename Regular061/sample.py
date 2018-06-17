import itertools

s = '1234'
n = [i for i in s]
ans = 0
##位置を使って順列を使う方法、
#print(n)
#exit
for i in range(3):
    print(i)
#rangeは0引数にした数までの要素をリストを返すっぽい
# +の個数
for i in range(len(n)):
    # +を入れるパターンを全探索
    for j in itertools.combinations(range(len(n)-1), i):
        print(i,'j', j)
        ##print('list',len(n)-1, i,  list(itertools.combinations(range(len(n)-1), i)))
        ##組み合わせのリストを返すっぽい
        temp = [i for i in s]
        #print('temp1', temp)
        # +を挿入
        for k in j[::-1]:
            temp.insert(k+1, "+")
            #print('temp3',k, temp)
        # list から 文字列に
        #print('temp2',temp)
        temp = "".join(temp)
        # +で区切ってリストに
        temp = temp.split("+")
        # リストの要素をint型に変換して総和を足す
        temp = map(int, temp)
        ans += sum(temp)
exit()
print(ans)
