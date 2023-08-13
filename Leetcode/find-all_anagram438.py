class Solution():
    def findAnagrams(self, s, p):
        pDict={}
        sDict={}
        result=[]
        pl=len(p)
        if len(p)>len(s): return result
        
        for c in p: pDict[c]=pDict.get(c,0)+1         
        
        start,end=0,pl
        for i in range(start,end):
            sDict[s[i]]=sDict.get(s[i],0)+1

        while end<=len(s):            
            if pDict==sDict: result.append(start)
                
            sDict[s[start]]-=1
            if sDict[s[start]]==0: del sDict[s[start]]
            if end<len(s):
                sDict[s[end]]=sDict.get(s[end],0)+1
                
            end+=1
            start+=1
        return result
    

resObj=Solution()
# s = "cbaebabacd"; p = "abc"
s = "abab"; p = "ab"
ans=resObj.findAnagrams(s,p)
print(ans)
    