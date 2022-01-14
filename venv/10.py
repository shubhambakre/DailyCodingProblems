# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
#
# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

def linearSearch(arr, n):
    for i in range(n):
        if arr[i] is i:
            return i
    # If no fixed point present then return -1
    return -1

# Driver program to check above functions
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(linearSearch(arr, n)))
