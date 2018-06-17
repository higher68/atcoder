n = int(input())
s = input()
num = [0 for i in range(n)]
for i in range(n):
    for j in range(0, i):
        if s[j] == "W":
            num[i] += 1
    for j in range(i+1, n):
        if s[j] == "E":
            num[i] += 1
    # print(num[i])
print(min(num))
