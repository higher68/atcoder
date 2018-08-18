# sortはネックになる
n = int(input())
x_tmp = input().split()
x = [[0 for i in range(n)] for j in range(3)]
for i in range(n):
    x[0][i] = int(x_tmp[i])
    x[1][i] = i
# print(x)
# sortは先に済ませておく
for i in range(3):
    print(x[i])
print('-'*20)
x = sorted(x, key=lambda y: y[3])
for i in range(3):
    print(x[i])
# print(x)
mid = n//2
for i in range(n):
    if i <= mid-1:
        x[2][i] = x[0][mid]
    else:
        x[2][i] = x[0][mid-1]
x = sorted(x, key=lambda y: y[1])
for i in range(n):
    print(x[2][i])
