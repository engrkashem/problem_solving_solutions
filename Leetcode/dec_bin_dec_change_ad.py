def changeAds(base10):
    bin=[]
    while base10>0:
        bin.append(base10%2)
        base10=int(base10/2)
        
    ans=[]
    for i in range(len(bin)-1,-1,-1):
        if bin[i]==0: ans.append(1)
        else:ans.append(0)
    
    result=0
    n=len(ans)-1
    for i in range(n, -1,-1):
        if ans[i]!=0:result+=2**(n-i)
    
    return result

base10=100
# base10=30
res=changeAds(base10)
print(res)