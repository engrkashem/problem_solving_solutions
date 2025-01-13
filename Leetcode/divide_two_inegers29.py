
class Solution:
    def divide(self, dividend, divisor):
        flag = 1

        if dividend < 0:
            flag *= -1
            dividend *= -1

        if divisor < 0:
            flag *= -1
            divisor *= -1

        a = dividend
        b = divisor
        result = 0
        while a >= divisor:
            result += 1
            a -= b

        return result*flag


obj = Solution()

# dividend = 10
# divisor = 3

# dividend = 7
# divisor = -3

# dividend = -7
# divisor = -3

dividend = -7
divisor = 3

print(obj.divide(dividend, divisor))
