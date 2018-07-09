a, b, c, x, y = map(int, input().split())
a_l = []


def abs0(inp):
    if inp < 0:
        return 0
    else:
        return inp


for i in range(x+1):
    # print(i, 2*(x-i), y-2*(x-i))
    a_l.append(a*i + c*2*(x-i) + b*abs0(y-(x-i)))
b_l = []
for i in range(y+1):
    # print(i, 2*(y-i), x-2*(y-i))
    b_l.append(b*i + c*2*(y-i) + a*abs0(x-(y-i)))
# print(a_l)
# print('-'*22)
# print(b_l)
# s = a_l + b_l
# print('-'*22)
# print(s)
print(min(a_l + b_l))
