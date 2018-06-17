n,y = map(int, input().split())
a = 0 #10000円札
b = 0 #5000円札
c = 0 #1000円札
#総当たりの発想自体はよかった。rangeの使い方が悪かった？
exist = False
for i in range(n+1):###range(x)のxは最後の数字だが、i=xになったら、forのところで終了。
#つまりi=xは実行されないらしい。r
    a = i
    if i != n:
        for j in range(n-i+1):
            b = j
            c = n - j - i
            sum = 10000*a +  5000*b + 1000*c
            if sum == y:
                print(a, b, c)
                exist = True
                break
            else:
                pass
    else :
        b = 0
        c = 0
        sum = 10000*a +  5000*b + 1000*c
        if sum == y:
            print(a, b, c)
            exist = True
            break
        else:
            pass
    if exist:
        break
if not exist:
    print(-1, -1, -1)
