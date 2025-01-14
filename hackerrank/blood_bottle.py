
test = int(input())
for _ in range(test):
    str = input()
    # ans = obj.solve(str)
    strList = str.split('0')
    treamedList = [i for i in strList if i != '']
    treamedList.sort()
    ans = 0
    for i in range(len(treamedList)-1, -1, -2):
        ans += len(treamedList[i])
    print(ans)
