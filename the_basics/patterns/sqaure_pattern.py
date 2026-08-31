# Time Complexity: O(n²) — two nested loops that both run exactly n times, so (n × n)
# Space Complexity: O(1) — uses a fixed amount of memory for the loop variables (i and j), regardless of the size of n.

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
    
    