# class Solution:
#     def isPrime(self, n):
#         count=0
#         for i in range(1,n+1):
#             if(n%i ==0):
#                 count+1
#         if(count > 2):
#             return "Not Prime" 
#         else:
#             return "Prime"      


# s1 = Solution()
# print(s1.isPrime(10))

#Using divisibility only up to its square root.
import math
class Solution:
    def isPrime(self, n):
        if n<=1: return "Not Prime"

        limit = int(math.sqrt(n))
        for i in range(2,limit+1):
            if(n%i ==0):
                return "Not Prime"
        else: 
            return "Prime"
              


s1 = Solution()
print(s1.isPrime(11))