class Solution:
    
    def reverseBits(self, n):
        result=0
        for i in range(32):
            lsb=(n>>i)&1

            result |= (lsb << (31-i))
            print(result)
        
        
        return result

obj=Solution()

inp = 0b00000010100101000001111010011100 

# inp = 11111111111111111111111111111101 


print(obj.reverseBits(inp))