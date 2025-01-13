# import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        mn,mx=1,max(piles)
        ans=mx
        
        while mn<=mx:
            k=(mn+mx)//2
            Required_time=0
            for pile in piles:
                if pile/k>pile//k:
                    Required_time+=pile//k +1
                else: Required_time+=pile//k 
            
            if Required_time<=h:
                ans=k
                mx=k-1
            else: mn=k+1
        
        return ans
    
obj=Solution()
# piles = [3,6,7,11]; h = 8
# piles = [30,11,23,4,20]; h = 5
piles = [30,11,23,4,20]; h = 6
print(obj.minEatingSpeed(piles,h))