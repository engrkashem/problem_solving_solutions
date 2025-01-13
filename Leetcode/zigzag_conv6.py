class Solution(object):
    def convert(self, s, numRows):
        res=""
        unit=numRows*2-2
        n=len(s)
        if numRows==1:
            return s
        
        for row in range(numRows):
            for char in range(n):
                if row==0 or row==numRows-1:
                    if unit*char+row<n:
                        res+=s[unit*char+row]
                else:
                    if unit*char+row<n:
                        res+=s[unit*char+row]
                    if unit*char+unit-row<n:
                        res+=s[unit*char+unit-row]
        return res
        
    
obj=Solution()
# s = "PAYPALISHIRING"; numRows = 3
s = "A"; numRows = 1
print(obj.convert(s,numRows))