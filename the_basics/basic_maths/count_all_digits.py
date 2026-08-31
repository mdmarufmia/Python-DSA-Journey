#Q-01: how you can extract the digits from the user and print them?

#Using Mathematical Method
num = int(input("Enter Number:"))
digits =[]

while num>0:
    digit = num %10
    digits.append(digit)
    num//=10
digits.reverse()
print(digits)

#Using List Comprehension method
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

