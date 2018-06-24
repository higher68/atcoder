s = input()
num = 0
for _ in s:
    if _ == '+':
        num += 1
    else:
        num -= 1
print(num)
