# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Snapchat.
#
# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
#
# The input list is not necessarily ordered in any way.
#
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

def mergeIntervals(arr):

        # Sorting based on the increasing order
        # of the start intervals
        arr.sort(key = lambda x: x[0])

        # array to hold the merged intervals
        m = []
        s = -10000
        max = -100000
        for i in range(len(arr)):
            a = arr[i]
            if a[0] > max:
                if i != 0:
                    m.append([s,max])
                max = a[1]
                s = a[0]
            else:
                if a[1] >= max:
                    max = a[1]

        #'max' value gives the last point of
        # that particular interval
        # 's' gives the starting point of that interval
        # 'm' array contains the list of all merged intervals

        if max != -100000 and [s, max] not in m:
            m.append([s, max])
        print("The Merged Intervals are :", end = " ")
        for i in range(len(m)):
            print(m[i], end = " ")

# Driver code
arr = [[1, 3], [5, 8], [5, 10], [4, 10],[20,25]]
mergeIntervals(arr)
