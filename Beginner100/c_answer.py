# 今回の問題は、3でかけた後の数に制限はかかってなかった。悲しい。
n = int(input())
a_tmp = input().split()
a = [[] for i in range(n)]
for i in range(n):
    a[i] = int(a_tmp[i])
a2 = [[] for i in range(n)]
for i in range(n):
    tmp = a[i]
    coun = 0
    while 1:
        if tmp % 2 == 0:
            tmp = tmp/2
            coun += 1
        else:
            break
    a2[i] = coun

print(sum(a2))
