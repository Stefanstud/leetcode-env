"""
You are given a **0-indexed** integer array `stations` of length `n`, where `stations[i]` represents the number of power stations in the `ith` city.

Each power station can provide power to every city in a fixed **range**. In other words, if the range is denoted by `r`, then a power station at city `i` can provide power to all cities `j` such that `|i - j| <= r` and `0 <= i, j <= n - 1`.

* Note that `|x|` denotes **absolute** value. For example, `|7 - 5| = 2` and `|3 - 10| = 7`.

The **power** of a city is the total number of power stations it is being provided power from.

The government has sanctioned building `k` more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers `r` and `k`, return *the **maximum possible minimum power** of a city, if the additional power stations are built optimally.*

**Note** that you can build the `k` power stations in multiple cities.
"""
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        $$$