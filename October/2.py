# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Epic.
#
# The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:
#
# 1
# 11
# 21
# 1211
# 111221
# As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
#
# Given an integer N, print the Nth term of this sequence.

class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        s = "11"
        for i in range(3, n + 1):

            # adding dummpy end of charter so that loop doesn't runs out of bound
            # and it counts the number of characters.
            s += "$"
            tmp = ""
            c = 1
            for j in range(1, len(s)):
                if (s[j] != s[j - 1]):
                    tmp += str(c + 0)
                    tmp += s[j - 1]
                    c = 1
                else:
                    c += 1
            s = tmp
        return s


my_new_instance = Solution()
print(my_new_instance.countAndSay(30))
