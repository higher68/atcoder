# &演算子は、bit形式には使えない。でも、数値には使える
d, g = map(int, input().split())
p = [[0, 0] for i in range(d)]
for i in range(d):
    p[i][0], p[i][1] = map(int, input().split())
## bit全探索

ans = 100000
for i in range(2 ** d):
    sum = 0
    ans_tmp = 0
    s = bin(i)
    #　得点の合計とそれまでの数を反映。
    for j in range(d):
        if bin(2 ** j) == bin(2 ** j & i):
            sum += p[j][0] * (j+1) * 100 + p[j][1]
            ans_tmp += p[j][0]
    if sum < g:
        for j in range(d-1, -1, -1):
            if bin(2 ** j) != bin(2 ** j & i):
                for k in range(p[j][0]-1):
                    sum += (j+1) * 100
                    ans_tmp += 1
                    if g <= sum:
                        break
                if g <= sum:
                    if ans_tmp < ans:
                        ans = ans_tmp
                    break
            else:
                continue
    else:
        if ans_tmp < ans:
            ans = ans_tmp
print(ans)
