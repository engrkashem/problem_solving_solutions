def dailyTemperatures(temperatures):
        st=[]
        op=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
                if len(st)==0:
                        st.append((t,i))
                        continue
                topTem=st[-1][0]
                # topDay=st[-1][1]
                while t>topTem and len(st)>0:
                        if t<=st[-1][0]:
                                break
                        temday=st.pop()
                        topTem=temday[0]
                        day=temday[1]
                        op[day]=i-day
                        # print(i,day, topTem, t)
                        
                st.append((t,i))
                # print(st)
        return op

     
# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
res=dailyTemperatures(temperatures)
print(res)