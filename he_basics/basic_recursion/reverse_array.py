def reverse_array(arr):
    if len(arr)<=1: return arr

    return [arr[-1]] + reverse_array(arr[:-1])

print(reverse_array([1,2,3,4,5]))
