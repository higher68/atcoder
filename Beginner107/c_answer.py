import math
n, k = map(int, input().split())
x_tmp = input().split()
x = [int(_) for _ in x_tmp]
ans = []


# 最適解は連続したk本のろうそくに順番に火をつける
# グラフを描いてみて、最適を探す時に連続したもののパターンがあったなと思い出せれば。。
def abs(x):
    '''絶対値をint型で返す
    return int-type abs-x
    '''
    return int(math.fabs(x))


for i in range(n-k+1):
    ans_left = abs(x[i]) + abs(x[i+k-1] - x[i])
    ans_right = abs(x[i+k-1]) + abs(x[i+k-1] - x[i])
    # ans.append(ans_left, ans_right)
    # listで追加したい場合には、extend
    ans.extend([ans_left, ans_right])
print(min(ans))
