#変数設定
##学び：rangeの使い方、pop()の使い方
n = input()
a = list(map(int, input().split()))
##list.pop(i)i番目の要素を削除、削除した値を返す
a_sum = 0
##Aliceの合計
b_sum = 0
##Bobの合計
##aでの最大値と、配列での番号
while a != []:
    #for 変数 in range([始まりの数値,] 最後の数値[, 増加する量]):1,5だと、1,2,3,4が出力される。
    #最大値のカードを求める
    a_max = a[0]
    i_max = 0
    for i in range(1, len(a)):
        if a_max < a[i]:
            a_max = a[i]
            i_max = i

    a_sum += a.pop(i_max)
    #print(a, a_sum)

    if a == []:
        break

    a_max = a[0]
    i_max = 0
    #print(len(a) , 'lena')
    for i in range(1, len(a)):###最後の値はlen(a)-1じゃない。注意!!!!
        #print('Hello')
        #print(a_max, a[i], 'loop')
        if a_max < a[i]:
            a_max = a[i]
            i_max = i

    b_sum += a.pop(i_max)
    #print(a, b_sum)

print(a_sum - b_sum)
