"""
There are `n` servers numbered from `0` to `n - 1` connected by undirected
server-to-server `connections` forming a network where `connections[i] = [ai,
bi]` represents a connection between servers `ai` and `bi`. Any server can
reach other servers directly or indirectly through the network.

A _critical connection_ is a connection that, if removed, will make some
servers unable to reach some other server.

Return all critical connections in the network in any order.
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        $$$
