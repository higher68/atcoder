k = int(input())
if k % 2 == 0:
    print((k//2) * (k//2))
else:
    print(((k-1)//2) * ((k-1)//2 + 1))