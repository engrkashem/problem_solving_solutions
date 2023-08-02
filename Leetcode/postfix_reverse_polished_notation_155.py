# import math

def evalRPN(tokens):
    stack=[]
    
    for i in tokens:
        
        if i=='+':
            top=int(stack.pop(-1))
            secondTop=int(stack.pop(-1))
            stack.append(top+secondTop)
        elif i=='-':
            top=int(stack.pop(-1))
            secondTop=int(stack.pop(-1))
            stack.append(secondTop-top)
        elif i=='*':
            top=stack.pop(-1)
            secondTop=stack.pop(-1)
            stack.append(int(top)*int(secondTop))
        elif i=='/':
            top=stack.pop(-1)
            secondTop=stack.pop(-1)
            stack.append(int(secondTop)/int(top))
        else:
            stack.append(i)
        # print(stack)
    
    return stack[0]


# tokens = ["4","13","5","/","+"]
# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res=evalRPN(tokens)
print(res)
# print((6/(-132)))
# print((6/(132)))
# print(math.ceil((6/(-132))))
# print(math.floor((6/(132))))
