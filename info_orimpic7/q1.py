money = int(input())
#これがなんでgeedyなのか⇨高い硬貨から払っていく⇨greedy
#半端な硬貨があったらだめぽい
c = []
c.append(500)
c.append(100)
c.append(50)
c.append(10)
c.append(5)
c.append(1)
submit_money = 1000
num = submit_money - money
def oturi(coin):
    global num
    for i in range(1, int(submit_money // coin)+1):
        sol = num - i * coin
        #print(sol, num, coin, i)
        if(sol < 0):
            num -= (i-1) * coin
            return i - 1
oturi_list = []
#print(c[0],type(c[0]))
for coin in c:
    oturi_list.append(oturi(coin))
#print(oturi_list[0],type(oturi_list[0]))
#exit()
sum = 0
for _ in oturi_list:
    sum += _
print(sum)
