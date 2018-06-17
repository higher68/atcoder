s = input()
d = 'dream', 'dreamer', 'erase', 'eraser'
d2 = []
for c in d:
    d2.append(c[::-1])

s = s[::-1]
print(d2)
print(s)
i = 0
judge = True
print(s[0:5],d2[0])
while 1 :
    print('i', i)
    if s[i:i+5] == d2[0]:
        i += 5
    elif s[i:i+7] == d2[1]:
        i += 7
    elif s[i:i+5] == d2[2]:
        i += 5
    elif s[i:i+6] == d2[3]:
        i += 6
    else:
        if i == len(s):
            break
        else:
            judge = False
            break

if judge:
    print('YES')
else:
    print('NO')
#for j in range(len(s)):
