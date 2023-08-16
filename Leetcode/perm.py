import math
def countPerms(n):
    ans=math.perm(3, n)
    return ans

# n=4
# n=3
n=2
# n=1
res=countPerms(n)
print(res)