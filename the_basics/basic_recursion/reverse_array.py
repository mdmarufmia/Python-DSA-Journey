#Using Recursive
def reverse_array(arr):
    if len(arr)<=1: return arr

    return [arr[-1]] + reverse_array(arr[:-1])

print(reverse_array([1,2,3,4,5]))


#Using Two-Pointer approach 
def reverse_(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[right],arr[left] = arr[left],arr[right]
        left+=1
        right-=1
    return arr
print(reverse_([1,2,3,4,5]))