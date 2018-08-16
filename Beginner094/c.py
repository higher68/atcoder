import copy
n = int(input())
x_tmp = input().split()
x = []
for _ in x_tmp:
    x.append(int(_))
num = n//2
for i in range(n):
    tmp_x = copy.copy(x)  # listを普通に代入すると、ディープコピーになる
    tmp_x.pop(i)  # pop(index)の出力は、削除した要素の値
    # その上で、popするとリスト自体も改変される
    # print(tmp_x)
    tmp_x = sorted(tmp_x, reverse=True)
    # print(tmp_x)
    print(tmp_x[num-1])
