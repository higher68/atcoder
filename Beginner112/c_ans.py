# 全探索可能
# 座標の候補は101 * 101 通り *100座標ぶんなので。
# 0の場合どうするか
# 0以外で候補を列挙して、あとで合ってるか検証(方針合ってた)


def abs(key):
    if key < 0:
        return -key
    else:
        return key


n = int(input())
x = [0] * n
y = [0] * n
h = [0] * n
for i in range(n):
    x[i], y[i], h[i] = map(int, input().split())
pos_max = 100  # 座標のmaxを定義
for posY in range(pos_max+1):
    for posX in range(pos_max+1):
        # needHは頂上がであるか判定する用
        # -1だとまだよくわからん
        # -2だと頂上ではない
        needH = -1
        # print("hoge", "posX", "posY", posX, posY)
        for i in range(n):
            if h[i] > 0:
                # この頂点からみて頂上がposX、posYの時
                # 頂上の高さを求める。
                tmp = h[i] + abs(posX-x[i]) + abs(posY-y[i])
                # print(i, "tmp", tmp)
                # print("h[i]", h[i], "x[i]", x[i], "y[i]", y[i])
                if needH == -1:
                    needH = tmp
                else:
                    if needH != tmp:
                        needH = -2
                        break
        # print(posX, posY, needH)
        # exit()
        if needH == -2:
            continue  # ダメだったら別の場所を探す
        # 高さが0の場合のチェック
        for i in range(n):
            if h[i] == 0:
                dist = abs(posX-x[i]) + abs(posY-y[i])
                if needH > dist:
                    needH = -2
                    break
        if needH == -2:
            continue
        print("{} {} {}".format(posX, posY, needH))
