s = input()
k = int(input())
sbst = set()
for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        sbst.add(s[j:j+i])
sbstl = sorted(list(sbst))
print(sbstl[k-1])
