class Solution:
    def intToRoman(self, num: int) -> str:
        ones=['','I','II','III','IV','V','VI','VII','VIII','IX']
        tens=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        hundreds=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        thousands=['','M','MM','MMM']
        romanNum=thousands[num//1000]+hundreds[(num%1000)//100]+tens[(num%100)//10]+ones[(num%10)]
        return romanNum
    
obj=Solution()
# num=50
num = 1994
print(obj.intToRoman(num))