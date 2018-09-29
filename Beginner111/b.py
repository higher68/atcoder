n = input()
if n[0] == n[1] and n[1] == n[2] and n[2] == n[0]:
    print(n)
else:
    n1 = int(n)
    n_tmp = int(n[0])
    n2 = n_tmp*100 + n_tmp*10 + n_tmp
    n3 = (n_tmp+1)*100 + (n_tmp+1)*10 + n_tmp+1
    if n2 >= n1:
        print(n2)
    else:
        print(n3)
