s = input()
sum = 0
n = [i for i in s]
#print(n)
l = len(n)

for i in range(2 ** (l-1)):
    #注意!!実際の組み合わせの数をbitに直したら１つ数が落ちる。
    #組み合わせのループ
    s1 = []
    for j in range(l):
        #bitshift用のループ
        if 1  & i >> j:
            s1.append(n[j])
            s1.append('+')
        else:
            s1.append(n[j])
    s2 = ''
    for i in s1:
        s2 += i
    s2 = s2.split('+')
    sum1 = 0
    for c in s2:
        sum1 += int(c)
    #print(sum1, s1)
    sum += sum1

print(sum)
