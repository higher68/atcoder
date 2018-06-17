##とりあえずinputしてみる。
n,a,b = map(int, input().split())
###count:条件を満たす数の総数、sum:各桁の和
##総和って、場合の数じゃなくて、数字の総和か。
sum = 0
##総当たりできるのが、PCの強みだよなあ。→1 to nで、一個ずつ足して行く、各桁を数を足す。
##初期条件
x = 1
##候補の数に総当たりするループ
while x <= n:
    #桁：digit
    digit_sum = 0
    tmp_x = x
    ##各桁の和を求める
    ##pythonは/=でなく!=
    while tmp_x != 0:
        ##%は余りを求める
        digit_sum += tmp_x % 10
        ##//は切り捨て演算
        tmp_x //= 10
    if a <= digit_sum  and digit_sum <= b:
        sum += x
    else:
        pass
    x += 1

print(sum)
