"""
You are given a string `s` consisting of digits from `1` to `9` and an integer `k`.

A partition of a string `s` is called **good** if:

* Each digit of `s` is part of **exactly** one substring.
* The value of each substring is less than or equal to `k`.

Return *the **minimum** number of substrings in a **good** partition of* `s`. If no **good** partition of `s` exists, return `-1`.

**Note** that:

* The **value** of a string is its result when interpreted as an integer. For example, the value of `"123"` is `123` and the value of `"1"` is `1`.
* A **substring** is a contiguous sequence of characters within a string.
"""
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        $$$