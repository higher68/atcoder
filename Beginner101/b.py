n = int(input())
num = []
tmp = n
while 1:
    if tmp == 0:
        break
    num.append(int(tmp % 10))
    tmp //= 10
s = sum(num)
if n % s == 0:
    print('Yes')
else:
    print('No')
