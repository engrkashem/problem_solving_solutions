
def trap(height):
    if not height:
        return 0
    
    left,right=0,len(height)-1
    maxL, maxR=height[left],height[right]
    ans=0
    
    while left<right:
        if maxL<maxR:
            left+=1
            maxL=max(maxL, height[left])
            ans+=maxL-height[left]
        else:
            right-=1
            maxR=max(maxR, height[right])
            ans+=maxR-height[right]
            
    return ans
        
    
                
        
        
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
res=trap(height)
print(res)