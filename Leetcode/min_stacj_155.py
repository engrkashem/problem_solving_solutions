class MinStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        minimum=self.stack[0]
        for n in self.stack:
            minimum=min(minimum,n)
        return minimum
        
        

obj=MinStack()
obj.push(3)
# obj.push(-2)
obj.push(4)
obj.push(6)
# obj.push(-1)
obj.push(9)
print(obj.stack)
obj.pop()
res=obj.top()
print(res)
print(obj.getMin())
