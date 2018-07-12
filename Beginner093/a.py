s = input()
sort_s = ''
for _ in sorted(s):
    sort_s += _
if sort_s == 'abc':
    print('Yes')
else:
    print('No')
