a, b = map(int, input().split())
i = b-a-1
li = 0
for _ in range(1, i+1):
    li += _
ans = li - a
print(ans)
