from heapq import heappop


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        for _ in range(32):
            count += xor & 1
            xor = xor >> 1
        return count