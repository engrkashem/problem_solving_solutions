class Solution:
    def findMin(self, nums):
        result=10**4
        left,right=0,len(nums)-1

        while(left<=right):
           
            if nums[left]<=nums[right]:
                result=min(result,nums[left])
                break

            mid=left+(right-left)//2

            if nums[left]<nums[mid]:
                result=min(result, nums[left])
                left=mid+1
                
            elif nums[right]>nums[mid]:
                result=min(result, nums[mid])
                right=mid-1
            else:
                result=min(result,nums[right])
                left=mid+1

        return result


                
    
obj=Solution()
nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# nums=[2,3,4,5,1]
# nums=[5,4,3,2,1]
# nums=[2,3,1]
# nums=[1]
print(obj.findMin(nums))


"""
class Solution:
    def findMin(self, nums):
        ans=10**5
        low,high=0,len(nums)-1
        
        while(low<=high):
            if(nums[low]<=nums[high]):
                ans=min(ans,nums[low])
                return ans
            
            mid=(high+low)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            elif nums[high]>=nums[mid]:
                ans=min(ans,nums[mid])
                high=mid-1
            # else:
            #     ans=min(ans,nums[high])
            #     low=mid+1
            
                
        return ans

"""
        