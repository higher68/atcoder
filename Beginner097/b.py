import math
x = int(input())
lis = [1]
for i in range(2, int(math.sqrt(x))+1):
    j = 2
    sample = 0
    while i ** j <= x:
        sample = i ** j
        j += 1
    if sample != 0:
        lis.append(sample)
print(max(lis))
