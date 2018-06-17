s1 = input()
t = input()
result = "UNRESTORABLE"
b = True
for i in range(len(s1) - len(t) + 1):
    for j in range(len(t)):
        if s1[i + j] != t[j] and s[i + j] != "?":
            break
        if j == len(t) - 1:
            s = (s1[:i] + t + s1[i + len(t):]).replace("?", "a")
            if b or s < result:
                #s< resultは辞書的に前に来るかどうか
                result = s
                b = False

print(result)
