s = input()
t = ''
d1 = 'dream'
d2 = 'dreamer'
e1 = 'erase'
e2 = 'eraser'
#s = s.replace(d1,'').replace(e1,'').replace(e2,'').replace(d2,'')
s.replace(e2,'').replace(e1,'').replace(d2,'').replace(d1,'')
#dreameraserの場合には、上ではerが残ってしまう。

if s:
    print('NO')
else:
    print('YES')












#l = len(s)
#i = 0
#accept = True
#print(s[i:i+5])
#スライスでi:i+5とすると、iからi+4まで書く
#exit()
#while s:
#    if s[i:i+5] == d1:
#        if s[i:i+7] == d2:
#            i += 7
#        else:
#            i += 5
#    elif s[i:i+5] == e1:
#        if s[i:i+7] == e2:
#        else:
#            i += 5
#    else:
#        accept = False

#    if accept == False:
#        break
#    print(i,l)
    #exit()で途中終了
#    if i == l:
#        break

#if accept == False:
#    print('NO')
#else:
#    print('YES')
