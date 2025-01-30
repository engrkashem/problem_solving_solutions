class Solution(object):
    def hammingWeight(self, n):
        
        return n.bit_count()
    
obj=Solution();

n = 11
# n = 128
# n = 2147483645
print(obj.hammingWeight(n))


"""
def hammingWeight(self, n):
        
        return bin(n).count("1")

def hammingWeight(self, n):
        count = 0
        while n:
            n &= (n - 1) 
            count += 1
        return count


def hammingWeight(self, n):
        res=[]
        self.getBinary(n, res)
        res="".join(map(str, res))
        res=res.replace("0","")
        return len(res)
    
    def getBinary(self, n, res):
        if n<=1:
            res.insert(0,n)
            return n
        
        res.insert(0,n%2)
        
        self.getBinary(n//2, res)

        return res

"""