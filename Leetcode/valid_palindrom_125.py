def isPalindrome( s):
    str=''
    sl=s.lower()
    for char in sl:
        c=ord(char)
        if (c>=65 and c<=90) or (c>=97 and c<=122) or (c>=48 and c<=57):
            str+=char
    
    i=0
    j=len(str)-1
    while(i<j):
        if str[i]!=str[j]:
            return False
        i+=1
        j-=1
    
    return True
    
    
    
# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = " "
res=isPalindrome(s)
print(res)
# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
print(ord('0'))
print(ord('9'))


