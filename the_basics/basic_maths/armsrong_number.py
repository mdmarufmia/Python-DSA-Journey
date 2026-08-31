class Solution:
    def isArmstrong(self, n):
        sum = 0
        while n>0:
            last_digit = n % 10
            sum+=pow(last_digit,3)
            n //= 10
            result = "Armstrong" if n == sum else "Not Armstrong"
            return result

s1 = Solution()
print(s1.isArmstrong(153))
