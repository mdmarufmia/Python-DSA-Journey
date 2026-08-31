import math
class Solution:
    def isArmstrong(self, n):
        _sum = 0
        original_n = n
        power = len(str(n))     #num of digits
        while n>0:
            last_digit = n % 10
            _sum+=last_digit ** power
            n //= 10
        result = "Armstrong" if original_n == _sum else "Not Armstrong"
        return result

s1 = Solution()
print(s1.isArmstrong(153))



#Another Way (Pythonic)
class Solution:
    def isArmstrong(self, n):
        num = str(n)
        power = len(num)
        total_sum = sum(int(digit) ** power for digit in num)

        result = "Armstrong" if n == total_sum else "Not Armstrong"
        return result

s1 = Solution()
print(s1.isArmstrong(1534))
