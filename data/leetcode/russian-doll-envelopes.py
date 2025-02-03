"""
You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi,
hi]` represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of
one envelope are greater than the other envelope's width and height.

Return _the maximum number of envelopes you can Russian doll (i.e., put one
inside the other)_.

**Note:** You cannot rotate an envelope.
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        $$$
