def processLogs(logs, threshold):
    ans={}
    result=[]
    for tranc in logs:
        tList=tranc.split(' ')
        u1=tList[0]
        u2=tList[1]
        if u1==u2:
            ans[u1]=ans.get(u1,0)+1
        else:
            ans[u1]=ans.get(u1,0)+1
            ans[u2]=ans.get(u2,0)+1
    for k,v in ans.items():
        if v>=threshold: result.append(k)
        
    return result

# logs=['1 2 50','1 7 70', '1 3 20', '2 2 17']
# threshold=2
logs=['9 7 50','22 7 20', '33 7 50', '22 7 30']
threshold=3
res=processLogs(logs, threshold)
print(res)