# This problem was asked by Apple.
#
# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
