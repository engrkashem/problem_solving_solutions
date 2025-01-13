
def mergeTwoLists( list1, list2):
    ans=[]
    while list1.next!=None:
        ans.append(list1.val)
        
    # for i in list2:
    #     ans.append(i)
    
    # ans.sort()
    return ans
    
    
    



# list1 = [1,2,4]
# list2 = [1,3,4]

# list1 = []
# list2 = []

list1 = []
list2 = [0]

res=mergeTwoLists(list1,list2)
print(res)