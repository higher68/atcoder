s = input()
t = input()
ans = 'No'
t2 = t + t
for i in range(len(t)):
    # print(i, t2[i:len(t)+i])
    if s == t2[i:len(t)+i]:
        print('Yes')
        exit()
print('No')
