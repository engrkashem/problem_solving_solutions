class Solution(object):
    def largestRectangleArea(self, heights):
        hlen=len(heights)
        # res=self.nextSmallerNumber(heights,hlen)
        # op: [1, -1, 4, 4, -1, -1]
        # res=self.prevSmallerNumber(heights,hlen)
        # op: [-1, -1, 1, 2, 1, 4]
        next=self.nextSmallerNumber(heights,hlen)
        prev=self.prevSmallerNumber(heights,hlen)
        area=-1
        for i in range(0,hlen):
            l=heights[i]
            if next[i]==-1: next[i]=hlen
            w=next[i]-prev[i]-1
            na=l*w
            area=max(area,na)
        return area
    
        
    
    def nextSmallerNumber(self,heights, n):
        st=[]
        st.append(-1)
        ans=[0]*n
        for i in range(n-1, -1, -1):
            cur=heights[i]
            while st[-1] != -1 and heights[st[-1]]>=cur:
                st.pop()
            ans[i]=st[-1]
            st.append(i)
        return ans
            
                
    
    def prevSmallerNumber(self,heights,n):
        st=[]
        st.append(-1)
        ans=[0]*n
        for i in range(0,n):
            cur=heights[i]
            while st[-1] != -1 and heights[st[-1]]>=cur:
                st.pop()
            ans[i]=st[-1]
            st.append(i)
        return ans
    

obj=Solution()
heights = [2,1,5,6,2,3]
# heights = [2,4]
res=obj.largestRectangleArea(heights)
print(res)