"""
A message containing letters from `A-Z` can be **encoded** into numbers using
the following mapping:

    
    
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    

To **decode** an encoded message, all the digits must be grouped then mapped
back into letters using the reverse of the mapping above (there may be
multiple ways). For example, `"11106"` can be mapped into:

  * `"AAJF"` with the grouping `(1 1 10 6)`
  * `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped
into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return _the **number** of ways to
**decode** it_.

The test cases are generated so that the answer fits in a **32-bit** integer.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        $$$
