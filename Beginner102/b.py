n = int(input())
a_tmp = input().split()
a = []
for i in range(n):
    a.append(int(a_tmp[i]))
print(max(a)-min(a))
