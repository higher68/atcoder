n = input()
n2 = ""
for _ in n:
    if _ == "1":
        n2 += "9"
    elif _ == "9":
        n2 += "1"
    else:
        n2 += _
print(n2)
