# sortはネックになる
n = int(input())
x_tmp = input().split()
x = [[0 for j in range(3)] for i in range(n)]
for i in range(n):
    x[i][0] = int(x_tmp[i])
    x[i][1] = i
# print(x)
# sortは先に済ませておく
# for i in range(n):
    # print(x[i])
    # print('-'*20)
x = sorted(x, key=lambda y: y[0])
# keyで指定すると、各行の2列目でsortしちゃう
# for i in range(n):
# print(x[i])
# print(x)
mid = n//2
for i in range(n):
    if i <= mid-1:
        x[i][2] = x[mid][0]
    else:
        x[i][2] = x[mid-1][0]
x = sorted(x, key=lambda y: y[1])
for i in range(n):
    print(x[i][2])
