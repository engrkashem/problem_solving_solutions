class Solution(object):
    def myAtoi(self, s):
        full=""
        strLen=len(s)
        i=0
        while i<strLen and s[i]==" ":
            i+=1
        
        neg, pos=None, None
        if i<strLen and s[i]=="-":
            neg=-1
            i+=1
        if i<strLen and s[i]=="+":
            i+=1
            pos=True
        
        while i<strLen and '0'<=s[i]<='9':
            full+=s[i]
            i+=1

        ans=0
        if full: ans=int(full)
        if pos and neg:
            return 0
        
        if neg:
            ans*=neg
            
        intMin=-2**31
        intMax=2**31-1
        if ans<intMin: return intMin
        if ans>intMax: return intMax
        
        return ans
            
        '''
        float_point=None
        newStr=""
        neg=None
        
        for c in s:
            if (ord(c)>=ord('0') and ord(c)<=ord('9')) or c=='.':
                newStr+=c
            if c=='-':
                neg=-1
        if '.' in newStr:
            float_point= newStr.index('.')                
        strLen=len(newStr)
        if float_point:right,i=float_point-1,1
        else: right,i=strLen-1,1
        ans=0
        while(right>=0):
            ans+=int(newStr[right])*i
            i*=10
            right-=1
        
        if float_point:
            left,j=float_point+1, 0.1
            while(left<strLen):
                ans+=int(newStr[left])*j
                j/=10
                left+=1
                
        if neg: 
            ans*=neg
            
        intMin=-2e31
        intMax=2e31-1
        if ans<intMin:
            return intMin
        if ans>intMax:
            return intMax
        
        return ans, newStr
    '''
    
# s = "420"
# s = "   -42"
# s = "4193 with words"
# s = "     -01234193.54300 with words"
s="words and 987"
# s="3.14159"
obj=Solution()
print(obj.myAtoi(s))