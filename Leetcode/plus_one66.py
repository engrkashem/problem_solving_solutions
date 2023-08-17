class Solution(object):
    def plusOne(self, digits):
        n=len(digits)
        ans=[0]*n
        flag=False
        rem=0
        for i in range(n-1, -1, -1):
            d=digits[i]
            if i==n-1 and d==9:
                # flag=True
                ans[i]=0
                rem=1
                continue
            
            if rem and d==9:
                ans[i]=0
                continue
            
            if i==n-1 and d!=9:
                ans[i]=d+1
                continue
                
            ans[i]=d+rem
            rem=0
        if rem:
            ans.insert(0,rem)
        return ans
                
                


# digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9]
digits = [9, 8,9,9,9,9,9,9,9]
obj=Solution()
res=obj.plusOne(digits)
print(res)