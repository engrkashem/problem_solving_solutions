def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closedN):
        print('recursively called..')
        if openN == closedN == n:
            print('OpenN=closeN=n is fullfilled..', stack)
            res.append("".join(stack))
            print('now res= ',res)
            return

        if openN < n:
            stack.append("(")
            print('openN=',openN,'open bracket added to stack ', stack)
            backtrack(openN + 1, closedN)
            stack.pop()
            print('open bracket popped from stack ', stack)
        if closedN < openN:
            stack.append(")")
            print('openN=',openN,'closeN=',closedN,'close bracket added to stack ', stack)
            backtrack(openN, closedN + 1)
            stack.pop()
            print('close bracket popped from stack ', stack)

    backtrack(0, 0)
    return res


res=generateParenthesis(3)
print(res)
# stack = ['(','(',')']
# res = []
# print(res)
# res.append("".join(stack))
# print(res)
