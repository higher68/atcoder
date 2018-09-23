import collections
s = input()
t = input()
loop = len(s)
s_col = collections.Counter(s)
t_col = collections.Counter(t)
# print("s_col", s_col)
s_l = sorted(s_col.values())
# print(len(s_col))
# print("s_l", s_l)
# print("t_col", t_col)
t_l = sorted(t_col.values())
# print("t_l", t_l)
# print(len(t_col))
if s_l == t_l:
    print("Yes")
else:
    print("No")
