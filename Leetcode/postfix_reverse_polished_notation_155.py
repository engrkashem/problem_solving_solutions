def evalRPN(tokens):
	stack=[]
	
	for i in tokens:
		if i=='*':
			stack.append(stack.pop()*stack.pop())
		elif i=='/':
			top=stack.pop()
			second=stack.pop()
			tf=1
			sf=1
			if top<0:
				tf=-1
			if second<0:
				sf=-1
			divRes=abs(second)//abs(top)
			stack.append(divRes*tf*sf)
		elif i=='+':
			stack.append(stack.pop()+stack.pop())
		elif i=='-':
			top=stack.pop()
			stack.append(stack.pop()-top)
		else:
			stack.append(int(i))
	
	return stack[-1]
			

# tokens = ["4","13","5","/","+"]
# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res=evalRPN(tokens)
print(res)

# print((6/(-132)))
# print((6/(132)))
# print(math.ceil((6/(-132))))
# print(math.floor((6/(132))))
