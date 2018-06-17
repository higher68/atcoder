###連続した文字列はlistで分割可能
s = map(int, list(input()))
x=0
for num in s:
    if num == 1:
        x += 1
    else:
        continue

print(x)
