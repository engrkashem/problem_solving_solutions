class Solution(object):
    
    def letterCombinations(self, digits):
        ans=[]
        phone_number_dict={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits: return []
        
        self.backTrack("",digits, ans, phone_number_dict)
        
        return ans
    
    def backTrack(self,comb,nxt_digits, ans, phone_number_dict):
        if len(nxt_digits)==0:
            ans.append(comb)
        else:
            for ltr in phone_number_dict[nxt_digits[0]]:
                self.backTrack(comb+ltr, nxt_digits[1:], ans, phone_number_dict)
        
        
        
    
    
obj=Solution()
digits = "23"
# digits = ""
# digits = "2"
print(obj.letterCombinations(digits))