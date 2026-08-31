n = 5  

# Top half 
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Print spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")    # Print stars
        else:
            print(" ", end="")    # Print inner spaces
    print()

# Bottom half 
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")  # Print spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")    # Print  stars
        else:
            print(" ", end="")    # Print inner spaces
    print()
