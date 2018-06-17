a, b = map(int, input().split())
lis = [a+b, a-b, a*b]
print(max(lis))
