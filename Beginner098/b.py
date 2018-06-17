n = int(input())
s = input()
n1 = []
for i in range(n):
    s1 = set()
    for j in range(i+1):
        for k in range(i+1, n):
            print(i, j, k, s[j], s[k])
            if s[j] == s[k] and set(s[j]).issubset(s1) is False:
                s1.add(s[j])
            print('len', len(s1))
    n1.append(len(s1))
print(max(n1))
