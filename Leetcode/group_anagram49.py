
from collections import defaultdict

def groupAnagrams(strs):
    # result=defaultdict(list)
    result={}
   
    for str in strs:
       
       countChar=[0]*26
       
       for char in str:
           countChar[ord(char)-ord('a')]+=1
        
       result[tuple(countChar)].update(str)
       print(result)
    
    # return result.values()
        
strs = ["eat","tea","tan","ate","nat","bat"]
result=groupAnagrams(strs)
# print(result)

