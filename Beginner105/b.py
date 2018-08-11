n = int(input())
l4 = n//4
l7 = n//7
judge = False

for i in range(l4+1):
    for j in range(l7+1):
        sum = i * 4 + j * 7
        if n == sum:
            judge = True
            break


if judge:
    print('Yes')
else:
    print('No')
