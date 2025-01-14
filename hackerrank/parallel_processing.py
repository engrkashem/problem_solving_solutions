def minTime(files, numCores, limit):
    files.sort()
    n = len(files)
    lim = limit
    resultantTime = 0
    for i in range(n-1, -1, -1):
        curNum = files[i]
        if curNum % numCores == 0 and lim:
            resultantTime += curNum//numCores
            lim -= 1
        else:
            resultantTime += curNum

    return resultantTime


files = [5, 3, 1]
numCores = 5
limit = 5

# files = [3, 1, 5]
# numCores = 1
# limit = 5

# files = [4, 1, 3, 2, 8]
# numCores = 4
# limit = 1

print(minTime(files, numCores, limit))
