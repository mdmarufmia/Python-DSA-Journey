#Q-01: Print name N times using recursion
def print_name(name,n):
    if n<=0: return
    print(name)
    print_name(name,n-1)

print_name("Maruf",10)


#Q-02: Print 1 to N times using recursion
def print_digit(n):
    if n<=0: return
    print_digit(n-1)
    print(n)

print_digit(10)


#Q-03: Print N to 1 times using recursion
def print_digit(n):
    if n<=0: return
    print(n)
    print_digit(n-1)

print_digit(10)


#Q-04: Print Sum of first N numbers
def calculate_sum(n):
    if n<=0: return 0
    return calculate_sum(n-1) + n

print(calculate_sum(100))


#Q-05: Print factorial of given num
def fact(n):
    if(n == 0 or n==1): return 1
    return fact(n-1) * n

print(fact(5))