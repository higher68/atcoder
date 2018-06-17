##500円玉の数
a = int(input())
##100円玉の数
b = int(input())
##50円玉の数
c = int(input())
##合計額
x = int(input())
##通り
count = 0

###xに対して使える500円玉の最大値を決定
max_a = int(x /500)
#print(max_a, a, b, c, x, count)
###500円玉の持ち数と理論上の最大値を比較
###maxが持ち数より多いと、持ち数までしか使えない
if max_a >= a:
    ###500円玉の使う数ごとに、100,50円玉の使える数を決定する
    for i in range(a+1):
        tmp_x1 = x - 500*i
        ###100円玉の使える数の理論上の最大値を決定
        max_b = int(tmp_x1 / 100)
            ###maxが持ち数より多いと、持ち数までしか使えない
        if max_b >= b:
            for j in range(b+1):
                tmp_x2 = tmp_x1 - 100 * j
                ###50円玉の必要な数を決定
                need_c = int(tmp_x2 / 50)
                ###needより持ち数が多いと、countできる
                if need_c <= c:
                    count += 1
                else:
                    continue
        ####maxが持ち数より少ないと、maxまでしか使えない
        else:
            for j in range(max_b+1):
                tmp_x2 = tmp_x1 - 100 * j
                ###50円玉の必要な数を決定
                need_c = int(tmp_x2 / 50)
                ###needより持ち数が多いと、countできる
                if need_c <= c:
                    count += 1
                else:
                    continue
####maxが持ち数より少ないと、maxまでしか使えない
else:
    ###rangeは、長さを表すので、
    for i in range(max_a+1):
        tmp_x1 = x - 500*i
        max_b = int(tmp_x1 / 100)
        if max_b >= b:
            for j in range(b+1):
                tmp_x2 = tmp_x1 - 100 * j

                ###50円玉の必要な数を決定
                need_c = int(tmp_x2 / 50)
                ###needより持ち数が多いと、countできる
                if need_c <= c:
                    count += 1
                else:
                    continue
        ####maxが持ち数より少ないと、maxまでしか使えない
        else:
            for j in range(max_b+1):
                tmp_x2 = tmp_x1 - 100 * j
                ###50円玉の必要な数を決定
                need_c = int(tmp_x2 / 50)
                ###needより持ち数が多いと、countできる
                if need_c <= c:
                    count += 1
                else:
                    continue
##output=何通りあるか
print(count)
