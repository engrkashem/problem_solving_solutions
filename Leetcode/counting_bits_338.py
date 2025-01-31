class Solution(object):
    def countBits(self, n):
        return [bin(i).count('1') for i in range(n+1)]
        # res = [0] * (n + 1)
        # i=1

        # while i<=n:
        #     res[i]=res[i>>1]+(i&1)
        #     i+=1

        # return res
    
    
obj=Solution()
# n = 2
# n = 5
n=7
print(obj.countBits(n))

"""
less efficient:
def countBits(self, n):
        res = [0] * (n + 1)
        i=1

        while i<=n:
            res[i]=self.get1bitsCount(i)
            i+=1

        return res
    
    def get1bitsCount(self, x):
        count=0
        while x!=0:
            x= x &(x-1)
            count += 1 

        return count

"""