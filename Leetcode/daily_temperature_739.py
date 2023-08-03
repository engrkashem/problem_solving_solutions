def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # n=len(temperatures)
        # ans=[0]*n
        
        # for i in range(n-1):
        #     diff=temperatures[i+1]-temperatures[i]
        #     if diff>0:
        #         ans[i]=diff
        
        # print(ans)
            
        
        
temperatures = [73,74,75,71,69,72,76,73]
res=dailyTemperatures(temperatures)
print(res)