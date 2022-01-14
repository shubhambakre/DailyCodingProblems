# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a sorted list of integers, square the elements and give the output in sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
def sortSquares(arr, n):
    left, right = 0, n - 1
    index = n - 1
    result = [0 for x in arr]

    while index >= 0:

        if abs(arr[left]) >= abs(arr[right]):
            result[index] = arr[left] * arr[left]
            left += 1
        else:
            result[index] = arr[right] * arr[right]
            right -= 1
        index -= 1

    for i in range(n):
        arr[i] = result[i]

# Driver code
arr = [-6, -3, -1, 2, 4, 5 ]
n = len(arr)

print("Before sort ")
for i in range(n):
    print(arr[i], end =" " )

sortSquares(arr, n)
print("\nAfter Sort ")
for i in range(n):
    print(arr[i], end =" " )
