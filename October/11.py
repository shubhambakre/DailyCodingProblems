# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Yahoo.
#
# Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of A -> B -> C, it should become A <- B <- C.

class Solution:
    def reverseGrpah(self,graph):
        rev = [[] for _ in range(len(graph))]

        for u, v in enumerate(graph):
            for k in v:
                rev[k].append(u)
        return rev
