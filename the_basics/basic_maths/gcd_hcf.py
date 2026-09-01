import math
result = math.gcd(48, 18)
print("GCD:", result)  



# Iterative Euclidean Algorithm
def gcd_iterative(a, b):    
    while b > 0:
        a, b = b, a % b
    return a

print("GCD:", gcd_iterative(18, 48))  



#Recursive Euclidean Algorithm
def gcd_recursive(a, b):    
    return a if b == 0 else gcd_recursive(b, a % b)

print("GCD:", gcd_recursive(48, 18))  

