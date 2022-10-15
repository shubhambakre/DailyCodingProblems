# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = float('inf')

        while(idx > 19):
            row = rand5()
            col = rand5()
            idx = col + (row - 1) * 5

        return 1 + (idx - 1)%7
