s = input()
s1 = ''
judge = False
if s[0] == 'A':
    for i in range(1,len(s)):
        s1 += s[i]
    jc = 0
    for i in range(1, len(s1)-1):
        if s1[i] == 'C':
            jc += 1
            s2 = ''
            for j in range(len(s1)):
                if j != i:
                    s2 += s1[j]
    if jc == 1:
        judge = True
    if judge:
        if s2.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
else:
    print('WA')
