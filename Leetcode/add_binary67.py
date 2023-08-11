
def addBinary( a, b):
    ans=''
    carry, i, j= 0,len(a)-1, len(b)-1
    
    while i>=0 or j>=0:
        sum=carry
        if i>=0: sum+=int(a[i])
        if j>=0: sum+=int(b[j])
        i,j=i-1,j-1
        carry=1 if sum>1 else 0
        ans+=str(sum%2)
        
    if carry != 0: ans += str(carry)
    
    return ans[::-1]
        


# a = "11"
# b = "1"

a = "1010"
b = "1011"

res=addBinary(a,b)
print(res)