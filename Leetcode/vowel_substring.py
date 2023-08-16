def vowelsubstring(s):
    al={'a':1,'e':1, 'i':1,'o':1, 'u':1}
    cl={}
    ans=0
    n=len(s)
    if n<5:
        return 0
    
    start,end=0,n
    consonent=0
    while start<end:
        for i in range(start,end):
            vowel=al.get(s[i],0)
            if vowel:
                cl[s[i]]=1
            else:
                consonent=i
                cl.clear()
                break
            if al==cl:
                ans+=1
                cl.clear()
                break
            
        if consonent!=0: start=i+1
        else:start+=1
    return ans
        
        

# s='aeioaexaaeuiou'
# s='aaeiouxa'
# s='axyzaeiou'
s='bcaekfaaeioau'
res=vowelsubstring(s)
print(res)