"""
Let's define a function `countUniqueChars(s)` that returns the number of
unique characters on `s`.

  * For example, calling `countUniqueChars(s)` if `s = "LEETCODE"` then `"L"`, `"T"`, `"C"`, `"O"`, `"D"` are the unique characters since they appear only once in `s`, therefore `countUniqueChars(s) = 5`.

Given a string `s`, return the sum of `countUniqueChars(t)` where `t` is a
substring of `s`.

Notice that some substrings can be repeated so in this case you have to count
the repeated ones too.
"""
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        $$$
