"""
You are given an array `routes` representing bus routes where `routes[i]` is a
bus route that the `ith` bus repeats forever.

  * For example, if `routes[0] = [1, 5, 7]`, this means that the `0th` bus travels in the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

You will start at the bus stop `source` (You are not on any bus initially),
and you want to go to the bus stop `target`. You can travel between bus stops
by buses only.

Return _the least number of buses you must take to travel from_`source`
_to_`target`. Return `-1` if it is not possible.
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        $$$
