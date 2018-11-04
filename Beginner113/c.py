n, m = map(int, input().split())
city = []
city_dict = {}
for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    city.append([tmp1, tmp2])
    if tmp1 not in city_dict.keys():
        city_dict[tmp1] = [tmp2]
    else:
        city_dict[tmp1].append(tmp2)
# for i in range(m):
#     print(i, city[i])
# for i in city_dict.keys():
#     print(i, city_dict[i])
for i in city_dict.keys():
    city_dict[i].sort()
    city_list = zip(city_dict[i], range(len(city_dict[i])))
    city_dict[i] = dict(city_list)

# for i in city_dict.keys():
#     for j in city_dict[i].keys():
#         print(city_dict[i][j])

for i in range(m):
    tmp1 = city[i][0]
    tmp2 = city[i][1]
    # print(tmp1, tmp2)
    # print("{:06}".format(tmp1))
    print("{:06}{:06}".format(tmp1, city_dict[tmp1][tmp2]+1))
