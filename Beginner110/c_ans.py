# 書く文字の変換が1対1対応でないと、スワップはできない
# 書いてどういう時にダメなのかやってみる？
# 各処理を分割してやってみる
s = input()
t = input()
# 変換逆変換の表を作る
trans_in = [-1] * 26  # 下の入力方式において、0はa→aで使う
trans_out = [-1] * 26
# 文字→asciiコード・・・ord・・・ordだと10進数変換してくれるみたいね
# asciiコード→文字・・・chr
for i in range(len(s)):
    a = ord(s[i]) - ord("a")
    b = ord(t[i]) - ord("a")
    # print(s[i], a)
    # print(t[i], b)
    if trans_in[a] != -1 or trans_out[b] != -1:
        if trans_in[a] != b or trans_out[b] != a:
            print("No")
            exit()
    trans_in[a] = b
    trans_out[b] = a
print("Yes")
