
def spiralOrder( matrix):
    row, col = len(matrix), len(matrix[0])
    t, r, b, l = 0, col-1, row-1 , 0
    ans = []

    while l <= r and t <= b:
        if l <= r:
            for i in range(l, r+1):
                ans.append(matrix[t][i]) 
            t += 1
        if t <= b:
            for i in range(t, b+1):
                ans.append(matrix[i][r]) 
            r -= 1
        if l <= r and t <= b:
            for i in range(r, l-1, -1):
                ans.append(matrix[b][i]) 
            b -= 1
        if t <= b and l <= r:
            for i in range(b, t-1, -1):
                ans.append(matrix[i][l]) 
            l += 1
    return ans
    # l,t,r,b = 0,0,len(matrix[0])-1,len(matrix)-1
    # ans=[]
    # while t<=b and l<=r:
    #     i,j=t,l
    #     while t<=b and j<=r:
    #         ans.append(matrix[i][j])
    #         j+=1
    #     t+=1
        
    #     i,j=t,r
    #     while i<=b and r>l:
    #         ans.append(matrix[i][j])
    #         i+=1
    #     if r>0:r-=1
        
    #     i,j=b,r
    #     while j>=l and b>=t:
    #         ans.append(matrix[i][j])
    #         j-=1
    #     if b>0:b-=1
        
    #     i,j=b,l
    #     while i>=t and l<r:
    #         ans.append(matrix[i][j])
    #         i-=1
    #     l+=1
    # return ans
            

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(len(matrix[0]))
res=spiralOrder(matrix)
print(res)
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 6]