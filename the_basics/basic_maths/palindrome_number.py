class Solution:
    def isPalindrome(self, n):
        reverse_num = int(str(n)[::-1])
        result = "Palindrome" if n == reverse_num else "Not Palindrome"
        return result

s1 = Solution()
print(s1.isPalindrome(131))