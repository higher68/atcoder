t = int(input())
s = [input()for i in range(t)]
# print(s)

for _ in range(t):
    ans = 0
    sn = len(s[_])
    # print('num', sn)
    if sn < 5:
        print(ans)
        continue
    i = 0
    while i+5 <= sn:
        # print(s[_][i:i+5])
        if s[_][i:i+5] == "tokyo" or s[_][i:i+5] == "kyoto":
            # print('hoge')
            ans += 1
            i += 5
        else:
            i += 1
    print(ans)
