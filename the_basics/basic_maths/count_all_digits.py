#Q-01: How can you extract the digits from the user and print them?

# Using a mathematical method
num = int(input("Enter Number:"))
digits =[]

while num>0:
    digit = num %10
    digits.append(digit)
    num//=10
digits.reverse()
print(digits)

# Using list comprehension method
num = int(input("Enter Number:"))
digits = [int(d) for d in str(num)]
print(digits)

#Or,
num = int(input("Enter Number:"))
for d in str(num):
    print(d,end=" ")


#Q-02: Count all the digits
num = int(input("Enter Number:"))
count = 0
for d in str(num):
    count+=1

print(count)

#Or
import math
num = int(input("Enter Number:"))
count = int(math.log10(num) + 1) if num>0 else 1
print(count)


#Or
num = int(input("Enter Number:"))
count = len(str(num))
print(count)


