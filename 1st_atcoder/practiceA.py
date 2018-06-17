a = int(input())

###スペース区切りの整数を作るため、mapの中にintを関数として引数にとり、かつinputの文字列を
##スペースで区切る
##mapは各要素への適用結果を返すイテレータを返す。
b, c = map(int, input().split())
s = input()
##python入門195参照。{} {}に何も指定しなければ、その順で出て、format内部は引数
print("{} {}".format(a+b+c, s))
