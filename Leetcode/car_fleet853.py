
def carFleet( target, position, speed):
    # x=sorted(zip(position, speed))
    x=zip(position, speed)
    y=list(x)
    y.sort()
    
    # time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
    time=[]
    for p,s in y:
        time.append((float(target-p)/s))
    
    ans=0
    curTime=0
    for t in time[::-1]:
        if t>curTime:
            ans+=1
            curTime=t
    
    return ans



# target = 12
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]

# target = 10
# position = [3]
# speed = [3]

target = 100
position = [0,2,4]
speed = [4,2,1]

res=carFleet(target=target, speed=speed, position=position)
print(res)