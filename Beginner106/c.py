s = input()
k = int(input())
if len(s) == 1:
    print(s)
else:
    i = 0
    while i <= k-1:
        if s[i] != '1':
            print(s[i])
            exit()
        else:
            i += 1
    print(1)
