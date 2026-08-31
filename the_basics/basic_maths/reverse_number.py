#Using Mathematical Logic
class Solution:
    def reverseNumber(self, n):
        reverse_num = 0
        while n>0:
            last_digit = n % 10
            reverse_num = (reverse_num * 10) + last_digit
            n //=10
        return reverse_num

s1 = Solution()
print(s1.reverseNumber(12345))


#Using Pythonic Way
class Solution:
    def reverseNumber(self, n):
        reverse_num = int(str(n)[::-1])
        return reverse_num

s1 = Solution()
print(s1.reverseNumber(12345))
