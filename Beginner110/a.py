a, b, c = map(int, input().split())

sol = []
sol.append(a*10+b+c)
sol.append(b*10+a+c)
sol.append(c*10+a+b)

print(max(sol))
