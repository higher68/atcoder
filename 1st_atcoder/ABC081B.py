##int標準入力はstr型なのに注意。
N = int(input())
##mapはリストには使えないのかな？別々の引数に結果を格納するっぽい？
A = list(map(int, input().split()))
judge = False
num = 0
## pythonではstopはexit
#exit()
while judge == False:
    i = 0
    for a in A:
        i += 1
        if a % 2 == 1:
            judge = True
            break
        else:
            A[i-1] /= 2
    if i == N:
        num += 1
print(num)
