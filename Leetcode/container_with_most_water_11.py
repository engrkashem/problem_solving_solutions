class Solution(object):
    def maxArea(self, height):
        left, right=0,len(height)-1
        max_area=0

        while left<right:
            width=right-left
            hight=min(height[left], height[right])
            current_area=width*hight
            max_area=max(max_area, current_area)

            if height[left]<= height[right]:
                left +=1
            else:
                right -=1

        return max_area
    
height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]

print(Solution().maxArea(height))

