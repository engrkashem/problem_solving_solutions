class Solution:
    
    def reverseBits(self, n):
        a=((n>>16)| (n<<16)) & 0xFFFFFFFF
        b=((a & 0xFF00FF00) >>8 | (a & 0x00FF00FF) <<8)
        c=((b & 0xF0F0F0F0) >>4 | (b & 0x0F0F0F0F) <<4)
        d=((c & 0xCCCCCCCC) >>2 | (c & 0x33333333) <<2)
        e=((d & 0xAAAAAAAA) >>1 | (d & 0x55555555) <<1)
        
        return e

obj=Solution()

# inp = 0b00000010100101000001111010011100 
inp = 0b10100000000000000000000000000000

# o/p 5

# inp = 11111111111111111111111111111101 


print(obj.reverseBits(inp))

"""

def reverseBits(self, n):
        result=0
        for i in range(16):
            leftBit=(n >>( 31 - i)) & 1
            rightBit=(n >> i) & 1
            
            result = (leftBit<<i) |  (rightBit<<(31-i)) | result
           
        return result

def reverseBits(self, n):
        result=0
        for i in range(32):
            lsb=(n>>i) & 1
            result |= (lsb << (31-i))

        return result

"""