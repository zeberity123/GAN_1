n = 5
ans = [[0 for _ in range(n)] for _ in range(n)]

cnt = [n-1]
while (n-1 > 0):
    cnt.append(n-1)
    cnt.append(n-1)
    n -= 1

col = 0
row = 0
v = 0
num = 1

for i in cnt:
    for _ in range(i):
        ans[col][row] = num
        num += 1
        if v == 0:
            row += 1
        if v == 1:
            col += 1
        if v == 2:
            row -= 1
        if v == 3:
            col -= 1
    if v == 3:
        v = 0
    else:
        v += 1
ans[col][row] = num

##############################

for i in ans:
    print(i)