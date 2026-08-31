#Case -01
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("-----------")


#Case -02
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("-----------")


#Case -03
n = 4
for i in range(1,n+1):
    num = 1
    for j in range(1,i+1):
        print(num, end=" ")
        num+=1
    print()
print("-----------")


#Case -04 (Floyd's Triangle)
n = 4
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num, end=" ")
        num+=1
    print()
print("-----------")


#Case -05 (Reverse Triangle)
n = 4 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
        i-=1
    print()
print("-----------")


#Case -06 (Inverted Triangle-Lower left) (Space & number printing)
n = 4 
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(i+1,end=" ")
    print()
print("-----------")


#Case -07 (Inverted Triangle-Upper Left) 
n = 4

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    num = 1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
print("-----------")


#Case -08 (Inverted Triangle) (Space & Character printing)
n = 4
char = 65
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(chr(char),end=" ")
    char +=1
    print()
print("-----------")
