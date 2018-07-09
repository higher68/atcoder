s = input()
price = 700
for i in range(len(s)):
    if s[i] == 'o':
        price += 100
    else:
        continue
print(price)
