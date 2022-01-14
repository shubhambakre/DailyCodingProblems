# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

def first_missing_positive(l):
    if not l:
        return 1
    for i in range(len(l)):
        while i + 1 != l[i] and 0 < l[i] <= len(l):
            v = l[i]
            l[i], l[v - 1] = l[v - 1], l[i]
            if l[i] == l[v - 1]:
                break
    for i in range(len(l)):
        if l[i] != i+1:
            return i+1
    return len(l) + 1

print(first_missing_positive([1,2,3]))
