h, w = map(int, input().split())
s = [[] for i in range(h)]
for i in range(h):
    s[i] = input()
s2 = [[False for j in range(w)] for i in range(h)]

ssum = 0
ssum2 = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            # print(i, j, s[i][j])
            if 0 < i:
                # print(s[i-1][j])
                if s[i-1][j] == "#":
                    s2[i][j] = True
            if i < h-1:
                # print(s[i+1][j])
                if s[i+1][j] == "#":
                    s2[i][j] = True
            if 0 < j:
                # print(s[i][j-1])
                if s[i][j-1] == "#":
                    s2[i][j] = True
            if j < w-1:
                # print(s[i][j+1])
                if s[i][j+1] == "#":
                    s2[i][j] = True
            if s2[i][j]:
                ssum2 += 1
            ssum += 1
if ssum == ssum2:
    print('Yes')
else:
    print('No')
