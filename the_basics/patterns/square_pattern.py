# Time Complexity: O(n²) — two nested loops that both run exactly n times, so (n × n)
# Space Complexity: O(1) — uses a fixed amount of memory for the loop variables (i and j), regardless of the size of n.

#Case-01
n = 4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
        j+=1
    print()
print("----------")


#Case -02 (Floyd's Square)
n = 4
num = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(num,end=" ")
        num+=1
    print()
print("----------")


#Case -03
n=4
char = 65
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(char),end=" ")
        char+=1
    print()
print("----------")


#Case -04
n=4
for i in range(1,n+1):
    char = 65
    for j in range(1,n+1):
        print(chr(char),end=" ")
        char+=1
    print()